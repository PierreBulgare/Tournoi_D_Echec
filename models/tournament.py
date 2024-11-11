import json
import os
from datetime import datetime
import settings

TOURNAMENTS_PATH = "data/tournaments/"


class Tournament:
    def __init__(self, name, location, start_date, end_date, description, total_rounds=4):
        self.name = name
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self.participants = []
        self.rounds = []
        self.current_round_number = 0

    def add_participant(self, player):
        """Ajoute un participant au tournoi"""
        if player.chess_id not in self.participants:
            self.participants.append(player)
        else:
            print("Ce joueur fait déjà parti de la liste des participants.")

    def add_round(self, round):
        """Ajoute un tour au tournoi"""
        if len(self.rounds) < self.total_rounds:
            self.rounds.append(round)
        else:
            print("Impossible d'ajouter ce tour. Le nombre maximal de tours est atteint.")

    @staticmethod
    def list_all_tournaments():
        """Retourne la liste de tous les joueurs sauvegardés."""

        # Initialise une liste qui va accueillir les instances de Tournament
        tournaments = []

        # Si le répertoire data/players existe
        if os.path.exists(TOURNAMENTS_PATH):
            for file_name in os.listdir(TOURNAMENTS_PATH):
                # Vérifie que le fichier est un fichier JSON
                if file_name.endswith(".json"):
                    # Récupère l'INE (Identidiant National d'Échecs) à partir du nom du fichier
                    tournament = Tournament.load(file_name.split('.')[0])
                    tournaments.append(tournament)

        return tournaments

    def save(self):
        """Enregistre les informations du joueur dans un fichier JSON"""

        # Crée le répertoire s'il n'existe pas
        os.makedirs(TOURNAMENTS_PATH, exist_ok=True)

        # Regroupe les informations dans un dictionnaire
        tournament_data = {
            "Nom": self.name,
            "Description": self.description,
            "Lieu": self.location,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "Nombre de tours": self.total_rounds,
            "Numéro du tour actuel": self.current_round_number,
            "Liste des participants": [player.chess_id for player in self.participants],
            "Liste des tours": [
                {
                    "Nom": round.name,
                    "Date et heure de début": round.start_datetime.strftime("%d-%m-%Y %H:%M"),
                    "Date et heure de fin": round.end_datetime.strftime("%d-%m-%Y %H:%M")
                    if round.end_datetime
                    else "Non terminé",
                    "Matchs": [
                        {
                            "Joueur1": {
                                "id": game["Joueur1"]["id"],
                                "couleur": game["Joueur1"]["couleur"],
                                "score": game["Joueur1"]["score"]
                            },
                            "Joueur2": {
                                "id": game["Joueur2"]["id"],
                                "couleur": game["Joueur2"]["couleur"],
                                "score": game["Joueur2"]["score"]
                            }
                        } for game in round.games
                    ]
                } for round in self.rounds
            ]

        }

        # Formate le nom du tournoi pour l'adapter en nom de fichier
        file_name = settings.format_file_name(self.name)

        # Nomme le fichier à partir de l'identifiant national d'échecs (ID.json)
        file_path = os.path.join(TOURNAMENTS_PATH, f"{file_name}-{self.start_date}.json")

        # Sauvegarde les informations du dictionnaire dans le fichier json
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tournament_data, file, ensure_ascii=False, indent=4)

        print(f"Les données du tournoi {self.name} ont été enregistré avec succès.")

    @staticmethod
    def load(name):
        """Charge un tournoi à partir d'un fichier JSON."""
        file_path = os.path.join(TOURNAMENTS_PATH, f"{settings.format_file_name(name)}.json")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le tournoi {name} n'existe pas.")

        with open(file_path, "r", encoding="utf-8") as file:
            tournament_data = json.load(file)
            tournament = Tournament(
                tournament_data["Nom"],
                tournament_data["Lieu"],
                tournament_data["Date de début"],
                tournament_data["Date de fin"],
                tournament_data["Description"],
                tournament_data["Nombre de tours"],
            )

            tournament.current_round_number = tournament_data["Numéro du tour actuel"]

            # Charger les participants en tant qu'objets Player
            from models.player import Player
            tournament.participants = [Player.load(chess_id) for chess_id in tournament_data["Liste des participants"]]

            # Charger les rounds
            from models.round import Round
            for round_data in tournament_data["Liste des tours"]:
                start_datetime = datetime.strptime(round_data["Date et heure de début"], "%d-%m-%Y %H:%M")
                round_instance = Round(round_data["Nom"])
                round_instance.start_datetime = start_datetime

                round_instance.end_datetime = datetime.strptime(
                    round_data["Date et heure de fin"], "%d-%m-%Y %H:%M"
                ) if round_data["Date et heure de fin"] != "Non terminé" else None

                # Charger les matchs avec seulement les identifiants des joueurs
                for game in round_data["Matchs"]:
                    player_one_id = game["Joueur1"]["id"]
                    player_two_id = game["Joueur2"]["id"]
                    player_one = Player.load(player_one_id)
                    player_two = Player.load(player_two_id)
                    round_instance.add_game(
                        player_one, game["Joueur1"]["couleur"], game["Joueur1"]["score"],
                        player_two,  game["Joueur2"]["couleur"], game["Joueur2"]["score"]
                    )

                tournament.rounds.append(round_instance)

            return tournament
