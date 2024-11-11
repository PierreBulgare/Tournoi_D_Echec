from datetime import datetime
from models.player import Player


class Round:
    def __init__(self, name):
        self.name = name
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self.games = []

    def add_game(self, player_one: Player, player_one_color: str, player_one_score: float,
                 player_two: Player, player_two_color: str, player_two_score: float):
        """Ajoute un match au tour"""
        self.games.append({
            "Joueur1": {"id": player_one.chess_id, "couleur": player_one_color, "score": player_one_score},
            "Joueur2": {"id": player_two.chess_id, "couleur": player_two_color, "score": player_two_score}
        })

    def end_round(self):
        """Enregistre la date et l'heure de fin du tour lorsqu'il est terminé"""
        self.end_datetime = datetime.now()
