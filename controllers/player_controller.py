import os
from models.player import Player
from views.player_view import PlayerView


class PlayerController:
    def check_player_exists(self, chess_id: str, error=True) -> bool:
        if os.path.exists(f"data/players/{chess_id}.json"):
            if error:
                print("Erreur ! Ce joueur existe déjà dans la base de donnée.")
            return True
        if not error:
            print("Erreur ! Ce joueur n'existe pas dans la base de donnée.")
        return False

    def find_player(self):
        chess_id = PlayerView.prompt_to_find_player(self)
        return chess_id

    def check_chess_id(self, chess_id: str) -> bool:
        # Vérifie si l'INE contient 7 caractères
        if len(chess_id) == 7:
            # Vérifie si uniquement les deux premiers catactères de l'INE sont des lettres
            if chess_id[:2].isalpha() and not chess_id[2:].isalpha():
                return True
            else:
                print("Erreur ! L'INE doit commencer par 2 lettres suivies de 5 chiffres.")
                return False
        else:
            print("Erreur ! L'INE doit contenir 7 caractères. 2 lettres suivies de 5 chiffres.")
            return False

    def check_name(self, name: str) -> bool:
        # Vérifie si le nom ou le prénom contient uniquement des lettres
        if name.isalpha():
            return True
        else:
            print("Erreur ! Le nom et prénom doivent être uniquement composés de lettres.")
            return False

    def add_player(self):
        """Ajoute un nouveau joueur en demandant les informations à l'utilisateur"""
        last_name, first_name, birth_date, chess_id = PlayerView.prompt_for_player_details(self)
        player = Player(chess_id, last_name, first_name, birth_date)
        # Sauvegarde les données du joueurs dans data/players
        player.save()
        print(f"Joueur {first_name} {last_name} ajouté avec succès.")

    def list_players(self):
        """Affiche la liste de tous les joueurs sauvegardés"""
        players = Player.list_all_players()
        PlayerView.display_players_list(players)

    def list_players_alphabetically(self):
        """Affiche la liste de tous les joueurs par ordre alphabétique."""
        players = Player.list_all_players()
        players_sorted = sorted(players, key=lambda p: p.last_name)  # Trier par nom de famille

        print("\nListe des joueurs par ordre alphabétique :")
        for player in players_sorted:
            print(f"{player.last_name}, {player.first_name} (INE: {player.chess_id})")
