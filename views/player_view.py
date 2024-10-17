import settings

class PlayerView:
    @staticmethod
    def display_player(player):
        """Affiche les informations d'un joueur"""
        print(f"Identifiant National d'Échecs : {player.chess_id}")
        print(f"Nom : {player.first_name} {player.last_name}")
        print(f"Date de naissance : {player.birth_date}")

    @staticmethod
    def display_players_list(players):
        """Affiche une liste de joueurs"""
        for player in players:
            print('-' * 20)
            PlayerView.display_player(player)

    @staticmethod
    def prompt_to_find_player(player_controller):
        """Demande à l'utiliser l'INE d'un joueur"""
        while True:
            chess_id = input("Identifiant National d'Échecs du joueur (ex. AB12345) : ")
            if not settings.check_empty(chess_id):
                if player_controller.check_chess_id(chess_id):
                    if player_controller.check_player_exists(chess_id, error = False):
                        break
        return chess_id
    
    @staticmethod
    def prompt_for_player_details(player_controller):
        """Demande à l'utilisateur d'entrer les informations d'un joueur"""
        
        # Identifiant Nationel d'Échecs
        while True:
            chess_id = input("Entrez l'identifiant national d'échecs (ex. AB12345) : ")
            if not settings.check_empty(chess_id):
                if player_controller.check_chess_id(chess_id):
                    if not player_controller.check_player_exists(chess_id):
                        break

        # Nom de Famille
        while True:
            last_name = input("Entrez le nom de famille du joueur : ")
            if not settings.check_empty(last_name):
                if player_controller.check_name(last_name):
                    break

        # Prénom
        while True:
            first_name = input("Entrez le prénom du joueur : ")
            if not settings.check_empty(first_name):
                if player_controller.check_name(first_name):
                    break

        # Date de Naissance
        while True:
            birth_date = input("Entrez la date de naissance (JJ-MM-AAAA) : ")
            if not settings.check_empty(birth_date):
                if settings.check_date(birth_date):
                    break

        return last_name, first_name, birth_date, chess_id