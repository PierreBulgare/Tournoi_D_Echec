from datetime import datetime
from models.player import Player

class Round:
    def __init__(self, name):
        self.name = name
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self.games = []

    def add_game(self, player_one: Player, player_one_score: int, player_two: Player, player_two_score: int):
        """Ajoute un match avec deux joueurs et leurs scores"""
        self.games.append(
            (
                [player_one.chess_id, player_one_score], 
                [player_two.chess_id, player_two_score])
            )

    def end_round(self):
        """Enregistre la date de fin du tour lorsqu'il est terminé"""
        self.end_datetime = datetime.now()