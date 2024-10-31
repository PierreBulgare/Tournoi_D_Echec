import json
import os

# Défini l'emplacement du répertoire contenant les informations des joueurs
PLAYERS_PATH = "data/players/"


class Player:
    def __init__(self, chess_id, last_name, first_name, birth_date):
        self.chess_id = chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.points = 0  # Total des points accumulés

    def add_points(self, points: float):
        """Ajoute des points au joueur."""
        self.points += points

    def save(self):
        """Enregistre les informations du joueur dans un fichier JSON"""

        # Crée le répertoire s'il n'existe pas
        os.makedirs(PLAYERS_PATH, exist_ok=True)

        # Regroupe les informations dans un dictionnaire
        player_data = {
            "Identifiant National d'Échecs": self.chess_id,
            "Nom": self.last_name,
            "Prénom": self.first_name,
            "Date de Naissance": self.birth_date
        }

        # Nomme le fichier à partir de l'Identifiant National d'Échecs (INE.json)
        file_path = os.path.join(PLAYERS_PATH, f"{self.chess_id}.json")

        # Sauvegarde les informations du dictionnaire dans le fichier json
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(player_data, file, ensure_ascii=False, indent=4)

        print(f"Les données de {self.first_name} {self.last_name} ont été enregistré avec succès.")

    @staticmethod
    def load(chess_id):
        """Charge les informations d'un joueur à partir d'un fichier JSON basé sur son identifiant national d'échecs"""

        file_path = os.path.join(PLAYERS_PATH, f'{chess_id}.json')

        # Si le fichier n'existe pas
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le joueur avec l'INE {chess_id} n'existe pas.")

        # Retourne une instance de Player avec les informations du JSON
        with open(file_path, "r", encoding="utf-8") as file:
            player_data = json.load(file)

        # Retourne une instance de Player
        return Player(
            chess_id=player_data["Identifiant National d'Échecs"],
            last_name=player_data["Nom"],
            first_name=player_data["Prénom"],
            birth_date=player_data["Date de Naissance"]
        )

    @staticmethod
    def list_all_players():
        """Retourne la liste de tous les joueurs sauvegardés."""

        # Initialise une liste qui va accueillir les instances de Player
        players = []

        # Si le répertoire data/players existe
        if os.path.exists(PLAYERS_PATH):
            for file_name in os.listdir(PLAYERS_PATH):
                # Vérifie que le fichier est un fichier JSON
                if file_name.endswith(".json"):
                    # Récupère l'INE (Identidiant National d'Échecs) à partir du nom du fichier
                    chess_id = file_name.split('.')[0]
                    player = Player.load(chess_id)
                    players.append(player)

        return players
