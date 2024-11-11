import os
from models.player import Player
from views.player_view import PlayerView

# Défini l'emplacement du répertoire contenant les informations des joueurs
PLAYERS_PATH = "data/players/"


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
        player = Player(chess_id.upper(), last_name.capitalize(), first_name.capitalize(), birth_date)
        # Sauvegarde les données du joueurs dans data/players
        player.save()
        print(f"Joueur {first_name} {last_name} ajouté avec succès.")

    def list_players(self):
        """Retourne une liste de tous les joueurs sauvegardés dans les fichiers JSON"""
        players = []
        if os.path.exists(PLAYERS_PATH):
            for file_name in os.listdir(PLAYERS_PATH):
                if file_name.endswith(".json"):
                    chess_id = file_name.split('.')[0]
                    try:
                        player = Player.load(chess_id)
                        players.append(player)
                    except FileNotFoundError:
                        print(f"Erreur : Le fichier {file_name} est introuvable.")

        PlayerView.display_players_list(players)

    def generate_players_list_alphabetically(self):
        """Génère la liste des joueurs par ordre alphabétique en TXT et HTML"""
        players = Player.list_all_players()
        players_sorted = sorted(players, key=lambda p: p.last_name)

        # Créer le dossier "reports" s'il n'existe pas
        os.makedirs("reports", exist_ok=True)
        file_path_txt = 'reports/liste_joueurs_alphabetique.txt'
        file_path_html = 'reports/liste_joueurs_alphabetique.html'

        with open(file_path_txt, 'w', encoding='utf-8') as file:
            file.write("Liste des joueurs par ordre alphabétique :\n")
            for player in players_sorted:
                file.write(f"{player.last_name.upper()} {player.first_name} (INE: {player.chess_id})\n")

        with open(file_path_html, 'w', encoding='utf-8') as file:
            file.write(
                '<html><head><meta charset="utf-8">'
                '<title>Liste des joueurs par ordre alphabétique</title>'
                '</head><body>'
                '<h1>Liste des joueurs par ordre alphabétique</h1><ul>'
            )
            for player in players_sorted:
                file.write(f"<li>{player.last_name} {player.first_name} (<b>INE</b>: {player.chess_id})</li>")
            file.write("</ul></body></html>")

        print(f"Rapports générés : \nTXT: {file_path_txt}\nHTML: {file_path_html}")
