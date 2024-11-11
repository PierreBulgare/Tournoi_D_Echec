import json
import os
import shutil

# Défini l'emplacement du répertoire contenant les informations des joueurs
PLAYERS_PATH = "data/players/"
TEMP_PATH = "temp/players"


class Player:
    def __init__(self, chess_id, last_name, first_name, birth_date, points=None):
        self.chess_id = chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        # Initialiser les points pour chaque tournoi comme un dictionnaire
        self.points = points if points else {}

    def add_points(self, tournament_name: str, points: float, tournament_date: str):
        """Ajoute des points pour un tournoi spécifique en utilisant la date du tournoi."""
        if tournament_name not in self.points:
            self.points[tournament_name] = {
                "date": tournament_date,
                "points": points
            }
        else:
            # Mettre à jour uniquement les points pour le tournoi en cours
            self.points[tournament_name]["points"] += points

    def save(self):
        """Enregistre les informations du joueur dans un fichier JSON"""
        os.makedirs(PLAYERS_PATH, exist_ok=True)
        # Inclure les points par tournoi dans les données du joueur
        player_data = {
            "Identifiant National d'Échecs": self.chess_id,
            "Nom": self.last_name,
            "Prénom": self.first_name,
            "Date de Naissance": self.birth_date,
            "Points": self.points  # Points par tournoi
        }
        file_path = os.path.join(PLAYERS_PATH, f"{self.chess_id}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(player_data, file, ensure_ascii=False, indent=4)
        print(f"Les données de {self.first_name} {self.last_name} ont été enregistrées avec succès.")

    @staticmethod
    def load(chess_id):
        """Charge les informations d'un joueur à partir d'un fichier JSON basé sur son identifiant national d'échecs"""
        file_path = os.path.join(PLAYERS_PATH, f'{chess_id}.json')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le joueur avec l'INE {chess_id} n'existe pas.")

        # Copie du fichier dans le dossier temporaire
        os.makedirs(TEMP_PATH, exist_ok=True)
        shutil.copy(file_path, os.path.join(TEMP_PATH, f'{chess_id}.json'))

        with open(file_path, "r", encoding="utf-8") as file:
            player_data = json.load(file)

        # Charger les points avec gestion des tournois
        points = player_data.get("Points", {})

        return Player(
            chess_id=player_data["Identifiant National d'Échecs"],
            last_name=player_data["Nom"],
            first_name=player_data["Prénom"],
            birth_date=player_data["Date de Naissance"],
            points=points
        )
