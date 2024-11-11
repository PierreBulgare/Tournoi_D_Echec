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
        if end_on >= start_on:
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

    def generate_tournaments_list(self):
        """Génère la liste de tous les tournois en TXT et HTML"""
        tournaments = Tournament.list_all_tournaments()

        # Créer le dossier "reports" s'il n'existe pas
        os.makedirs("reports", exist_ok=True)
        file_path_txt = 'reports/liste_tournois.txt'
        file_path_html = 'reports/liste_tournois.html'

        # Fichier TXT
        with open(file_path_txt, 'w', encoding='utf-8') as file:
            file.write("Liste des tournois :\n")
            for tournament in tournaments:
                file.write(
                    f"{tournament.name} - Lieu : {tournament.location}"
                    f"(Début : {tournament.start_date}, Fin : {tournament.end_date})\n"
                )

        # Fichier HTML
        with open(file_path_html, 'w', encoding='utf-8') as file:
            file.write('<html><head><meta charset="utf-8"><title>Liste des tournois</title></head><body>')
            file.write("<h1>Liste des tournois</h1><ul>")
            for tournament in tournaments:
                file.write(
                    f"<li><b>{tournament.name}</b><br>- Lieu : {tournament.location}"
                    f"<br>- Date de Début : {tournament.start_date}"
                    f"<br>- Date de Fin : {tournament.end_date}</li>"
                )
            file.write("</ul></body></html>")

        print(f"Rapports générés : \nTXT: {file_path_txt}\nHTML: {file_path_html}")

    def generate_tournament_datas(self):
        """Génère le nom et les dates d'un tournoi en TXT et HTML"""
        tournament_name, tournament_date = TournamentView.prompt_to_find_tournament(self)
        tournament = Tournament.load(f"{settings.format_file_name(tournament_name)}-{tournament_date}")

        os.makedirs("reports", exist_ok=True)
        file_path_txt = f'reports/{tournament_name}_{tournament.start_date}.txt'
        file_path_html = f'reports/{tournament_name}_{tournament.start_date}.html'

        # Fichier TXT
        with open(file_path_txt, 'w', encoding='utf-8') as file:
            file.write(f"Tournoi : {tournament.name}\n")
            file.write(f"Lieu : {tournament.location}\n")
            file.write(f"Date de début : {tournament.start_date}\n")
            file.write(f"Date de fin : {tournament.end_date}\n")

        # Fichier HTML
        with open(file_path_html, 'w', encoding='utf-8') as file:
            file.write('<html><head><meta charset="utf-8"><title>Tournoi - Dates</title></head><body>')
            file.write(f"<h1>Tournoi : {tournament.name}</h1>")
            file.write(f"<p>Lieu : {tournament.location}</p>")
            file.write(f"<p>Date de début : {tournament.start_date}</p>")
            file.write(f"<p>Date de fin : {tournament.end_date}</p>")
            file.write("</body></html>")

        print(f"Rapports générés : \nTXT: {file_path_txt}\nHTML: {file_path_html}")

    def generate_tournament_players_alphabetically(self):
        """Génère la liste des joueurs d'un tournoi par ordre alphabétique en TXT et HTML"""
        tournament_name, tournament_date = TournamentView.prompt_to_find_tournament(self)
        tournament = Tournament.load(f"{settings.format_file_name(tournament_name)}-{tournament_date}")
        sorted_players = sorted(tournament.participants, key=lambda p: p.last_name)

        os.makedirs("reports", exist_ok=True)
        file_path_txt = f'reports/{tournament_name}_joueurs_alphabetique.txt'
        file_path_html = f'reports/{tournament_name}_joueurs_alphabetique.html'

        # Fichier TXT
        with open(file_path_txt, 'w', encoding='utf-8') as file:
            file.write(f"Liste des joueurs du tournoi '{tournament.name}' (ordre alphabétique) :\n")
            for player in sorted_players:
                file.write(f"{player.last_name} {player.first_name} (INE: {player.chess_id})\n")

        # Fichier HTML
        with open(file_path_html, 'w', encoding='utf-8') as file:
            file.write('<html><head><meta charset="utf-8"><title>Joueurs du Tournoi</title></head><body>')
            file.write(f"<h1>Joueurs du tournoi '{tournament.name}'</h1><ul>")
            for player in sorted_players:
                file.write(f"<li>{player.last_name} {player.first_name} (<b>INE</b>: {player.chess_id})</li>")
            file.write("</ul></body></html>")

        print(f"Rapports générés : \nTXT: {file_path_txt}\nHTML: {file_path_html}")

    def generate_tournament_rounds_and_games(self):
        """Génère la liste des tours et des matchs d'un tournoi en TXT et HTML"""
        tournament_name, tournament_date = TournamentView.prompt_to_find_tournament(self)
        tournament = Tournament.load(f"{settings.format_file_name(tournament_name)}-{tournament_date}")

        os.makedirs("reports", exist_ok=True)
        file_path_txt = f'reports/{tournament_name}_tours_et_matchs.txt'
        file_path_html = f'reports/{tournament_name}_tours_et_matchs.html'

        # Fichier TXT
        with open(file_path_txt, 'w', encoding='utf-8') as file:
            file.write(f"Tours et matchs du tournoi '{tournament.name}' :\n")
            for round in tournament.rounds:
                start_time = round.start_datetime.strftime("%d-%m-%Y %H:%M")
                end_time = round.end_datetime.strftime("%d-%m-%Y %H:%M") if round.end_datetime else "En cours"
                file.write(f"\n{round.name} - Début : {start_time}, Fin : {end_time}\n")
                for game in round.games:
                    player1 = game["Joueur1"]
                    player2 = game["Joueur2"]
                    file.write(
                        f"  Match: {player1['id']} ({player1['couleur']}, Score: {player1['score']}) vs "
                        f"{player2['id']} ({player2['couleur']}, Score: {player2['score']})\n"
                    )

        # Fichier HTML
        with open(file_path_html, 'w', encoding='utf-8') as file:
            file.write('<html><head><meta charset="utf-8"><title>Tours et Matchs du Tournoi</title></head><body>')
            file.write(f"<h1>Tours et matchs du tournoi '{tournament.name}'</h1>")

            for round in tournament.rounds:
                start_time = round.start_datetime.strftime("%d-%m-%Y %H:%M")
                end_time = round.end_datetime.strftime("%d-%m-%Y %H:%M") if round.end_datetime else "En cours"
                file.write(f"<h2>{round.name} - Début : {start_time}, Fin : {end_time}</h2>")
                for game in round.games:
                    player1 = game["Joueur1"]
                    player2 = game["Joueur2"]
                    file.write(
                        f"<p>Match: {player1['id']} ({player1['couleur']}, Score: {player1['score']}) vs "
                        f"{player2['id']} ({player2['couleur']}, Score: {player2['score']})</p>"
                    )

            file.write("</body></html>")

        print(f"Rapports générés : \nTXT: {file_path_txt}\nHTML: {file_path_html}")

    def add_player_to_tournament(self, player_controller):
        """Ajoute un joueur à un tournoi existant"""
        tournament_name = self.find_tournament()
        chess_id = player_controller.find_player()
        tournament = Tournament.load(tournament_name)
        if not self.check_player_exists(tournament.participants, chess_id):
            player = Player.load(chess_id.upper())
            tournament.add_participant(player)
            tournament.save()
            print(f"Joueur {player.first_name} {player.last_name} ajouté au tournoi [{tournament.name}].")

    def add_multiple_players_to_tournament(self, player_controller):
        """Ajoute plusieurs joueurs à un tournoi existant en demandant les identifiants INE des joueurs."""
        tournament_name = self.find_tournament()
        tournament = Tournament.load(tournament_name)

        # Demander à l'utilisateur d'entrer plusieurs INE séparés par une virgule
        chess_ids = input("Entrez identifiants des joueurs, séparés par des virgules : ").split(',')

        # Supprimer les espaces inutiles autour des identifiants
        chess_ids = [chess_id.strip().upper() for chess_id in chess_ids]

        for chess_id in chess_ids:
            # Vérifier si le joueur existe dans la base de données
            if player_controller.check_player_exists(chess_id, error=False):
                # Charger le joueur et ajouter au tournoi s'il n'est pas déjà inscrit
                player = Player.load(chess_id)
                if not self.check_player_exists(tournament.participants, chess_id):
                    tournament.add_participant(player)
                    print(f"Joueur {player.first_name} {player.last_name} ajouté au tournoi.")
                else:
                    print(f"Le joueur {player.first_name} {player.last_name} est déjà inscrit dans le tournoi.")
            else:
                print(f"L'identifiant INE {chess_id} n'existe pas dans la base de données des joueurs.")

        # Sauvegarder les modifications du tournoi
        tournament.save()
        print("Tous les joueurs valides ont été ajoutés au tournoi.")

    def add_round_to_tournament(self):
        """Ajoute un nouveau tour au tournoi en triant les joueurs par points et en évitant les matchs identiques."""
        tournament_name = self.find_tournament()
        tournament = Tournament.load(tournament_name)

        # Vérifier si le dernier round est terminé
        if tournament.rounds:
            last_round = tournament.rounds[-1]
            if last_round.end_datetime is None:
                print(f"Impossible de créer un nouveau round : le {last_round.name} est encore en cours.")
                return

        round_name = f"Round {len(tournament.rounds) + 1}"
        new_round = Round(round_name)

        # Récupère les matchs déjà joués pour éviter les doublons
        game_played = set()
        for past_round in tournament.rounds:
            for game in past_round.games:
                player1, player2 = game["Joueur1"]["id"], game["Joueur2"]["id"]
                game_played.add(frozenset([player1, player2]))

        # Trier les joueurs par points (et mélanger pour les égalités)
        players = sorted(
            tournament.participants,
            key=lambda p: (p.points.get(tournament.name, {}).get("points", 0), random.random()),
            reverse=True
        )

        i = 0
        games_added = False  # Pour vérifier si des matchs ont été ajoutés

        while i < len(players) - 1:
            player1 = players[i]
            player2 = players[i + 1]

            # Vérifier si cette paire a déjà joué ensemble
            if frozenset([player1.chess_id, player2.chess_id]) not in game_played:
                # Tirage au sort pour blanc et noir
                if random.choice([True, False]):
                    white, black = player1, player2
                else:
                    white, black = player2, player1

                # Ajouter le match avec les couleurs assignées
                new_round.add_game(white, "Blanc", 0, black, "Noir", 0)
                game_played.add(frozenset([white.chess_id, black.chess_id]))
                games_added = True
                i += 2  # Passer aux joueurs suivants
            else:
                # Si la paire a déjà été jouée, essayer une autre paire
                j = i + 2
                while j < len(players):
                    player2 = players[j]
                    if frozenset([player1.chess_id, player2.chess_id]) not in game_played:
                        # Ajouter la paire alternative
                        if random.choice([True, False]):
                            white, black = player1, player2
                        else:
                            white, black = player2, player1

                        new_round.add_game(white, "Blanc", 0, black, "Noir", 0)
                        game_played.add(frozenset([white.chess_id, black.chess_id]))
                        games_added = True
                        players.pop(j)  # Supprimer player2 pour éviter les doublons dans le tour
                        break
                    j += 1
                i += 1  # Passer au joueur suivant si aucune paire n'a été trouvée

        # Enregistrer le round si des matchs ont été créés
        if games_added:
            tournament.add_round(new_round)
            tournament.current_round_number += 1
            tournament.save()
            print(f"{round_name} ajouté au tournoi {tournament.name}.")
        else:
            print(f"Aucune paire valide disponible. Le tournoi {tournament.name} est terminé.")
            tournament.save()

    def end_round(self):
        """Demande l'issue du tour, met à jour les points des joueurs, et termine le round"""
        tournament_name = self.find_tournament()
        tournament = Tournament.load(tournament_name)
        print("Numéro du tour actuel avant fin de tour :", tournament.current_round_number)

        if not tournament.rounds:
            print("Aucun tour n'a encore été joué pour ce tournoi.")
            return

        current_round = tournament.rounds[-1]
        tournament_display_name = tournament.name

        for game in current_round.games:
            # Accéder aux informations des joueurs pour chaque match
            player_one_id = game["Joueur1"]["id"]
            player_two_id = game["Joueur2"]["id"]

            # Conserver la couleur d'origine
            player_one_color = game["Joueur1"]["couleur"]
            player_two_color = game["Joueur2"]["couleur"]

            # Demander si c'est une égalité
            while True:
                result = input(
                        f"Le match entre {player_one_id} et {player_two_id} est-il une égalité ? (o/n) : "
                    ).strip().lower()
                if result in ('o', 'n'):
                    break
                else:
                    print("Entrée invalide. Veuillez répondre par 'o' pour oui ou 'n' pour non.")

            # Mettre à jour les scores sans changer la couleur
            if result == 'o':
                game["Joueur1"]["score"] = 0.5
                game["Joueur2"]["score"] = 0.5
            else:
                winner_id = input(f"Qui est le gagnant ? ({player_one_id}/{player_two_id}) : ").strip()
                if winner_id == player_one_id:
                    game["Joueur1"]["score"] = 1
                    game["Joueur2"]["score"] = 0
                elif winner_id == player_two_id:
                    game["Joueur1"]["score"] = 0
                    game["Joueur2"]["score"] = 1
                else:
                    print("Entrée invalide, réessayez.")
                    continue

            # Assurer la couleur d'origine
            game["Joueur1"]["couleur"] = player_one_color
            game["Joueur2"]["couleur"] = player_two_color

        # Enregistrer les points des joueurs pour le tournoi
        for game in current_round.games:
            player_one_id = game["Joueur1"]["id"]
            player_one_score = game["Joueur1"]["score"]
            player_two_id = game["Joueur2"]["id"]
            player_two_score = game["Joueur2"]["score"]

            # Charger les objets Player et mettre à jour les scores
            player_one = Player.load(player_one_id)
            player_two = Player.load(player_two_id)
            player_one.add_points(tournament_display_name, player_one_score, tournament.start_date)
            player_two.add_points(tournament_display_name, player_two_score, tournament.start_date)
            player_one.save()
            player_two.save()

        current_round.end_round()
        print("Numéro du tour actuel après  fin de tour :", tournament.current_round_number)
        tournament.save()
        print(f"Le round {current_round.name} est maintenant terminé.")
