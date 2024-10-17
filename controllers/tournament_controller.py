import os
from datetime import datetime
import random
import settings
from models.tournament import Tournament
from models.round import Round
from views.tournament_view import TournamentView
from models.player import Player


class TournamentController:
    def check_tournament_exists(self, name: str, date: str, error=True) -> bool:
        if os.path.exists(f"data/tournaments/{settings.format_file_name(name)}-{date}.json"):
            if error:
                print("Erreur ! Ce tournoi existe déjà dans la base de donnée.")
            return True
        if not error:
            print("Erreur ! Ce tournoi n'existe pas !")
        return False

    def check_player_exists(self, participants, chess_id):
        if chess_id in [player.chess_id for player in participants]:
            print("Erreur ! Ce joueur est déjà inscrit pour ce tournoi.")
            return True
        return False

    @staticmethod
    def compare_dates(start_date: str, end_date: str) -> bool:
        date_format = "%d-%m-%Y"
        start_on = datetime.strptime(start_date, date_format)
        end_on = datetime.strptime(end_date, date_format)
        if end_on > start_on:
            return True
        else:
            print("Erreur ! La date de fin ne peut pas se situer avant la date de début du tournoi.")
            return False

    def create_tournament(self):
        """Crée un nouveau tournoi en demandant les informations à l'utilisateur"""
        name, location, start_date, end_date, description = TournamentView.prompt_for_tournament_details()
        tournament = Tournament(name, location, start_date, end_date, description)
        tournament.save()
        print(f"Tournoi {name} créé avec succès.")

    def find_tournament(self):
        name, date = TournamentView.prompt_to_find_tournament(self)
        return f"{settings.format_file_name(name)}-{date}"

    def list_tournaments(self):
        """Affiche la liste des tournois"""
        tournaments = Tournament.list_all_tournaments()
        TournamentView.display_tournaments(tournaments)

    def add_player_to_tournament(self, player_controller):
        """Ajoute un joueur à un tournoi existant"""
        tournament_name = self.find_tournament()
        chess_id = player_controller.find_player()
        tournament = Tournament.load(tournament_name)
        if not self.check_player_exists(tournament.participants, chess_id):
            player = Player.load(chess_id)
            tournament.add_participant(player)
            tournament.save()
            print(f"Joueur {player.first_name} {player.last_name} ajouté au tournoi [{tournament.name}].")

    def add_round_to_tournament(self):
        """Ajoute un nouveau tour au tournoi avec des paires générées dynamiquement."""
        tournament_name = self.find_tournament()
        tournament = Tournament.load(tournament_name)

        if len(tournament.participants) >= 2:
            round_name = f"Round {len(tournament.rounds) + 1}"
            new_round = Round(round_name)

            # Récupère les matchs déjà joués pour éviter les doublons
            game_played = set()
            for past_round in tournament.rounds:
                for game in past_round.games:
                    player1, player2 = game[0][0], game[1][0]
                    game_played.add(frozenset([player1, player2]))

            players = tournament.participants.copy()
            random.shuffle(players)

            i = 0
            max_attempts = 10  # Limiter les tentatives pour éviter les boucles infinies
            attempts = 0
            games_added = False  # Nouveau booléen pour vérifier si des jeux sont ajoutés

            while i < len(players) and attempts < max_attempts:
                if i + 1 >= len(players):
                    print("Pas assez de joueurs disponibles pour former une paire supplémentaire.")
                    break

                player1 = players[i]
                player2 = players[i + 1]

                # Vérifier que le match n'a pas déjà eu lieu
                if frozenset([player1.chess_id, player2.chess_id]) not in game_played:
                    new_round.add_game(player1, 0, player2, 0)
                    i += 2  # Passer aux deux joueurs suivants
                    games_added = True  # Marquer que des paires ont été ajoutées
                else:
                    # Si le match a déjà eu lieu, remélanger et recommencer
                    random.shuffle(players)
                    i = 0  # Réinitialise l'index pour recommencer la génération
                    attempts += 1

            if attempts == max_attempts:
                print("Impossible de générer un nouveau tour sans doublon après plusieurs tentatives.")

            # Ajouter le round seulement si des matchs ont été ajoutés
            if games_added:
                tournament.add_round(new_round)
                tournament.save()
                print(f"{round_name} ajouté au tournoi {tournament.name}.")
            else:
                print("Aucun tour n'a été ajouté, aucun match valide n'a pu être généré.")
        else:
            print("Erreur ! Ce tournoi n'a pas assez de participants.")
