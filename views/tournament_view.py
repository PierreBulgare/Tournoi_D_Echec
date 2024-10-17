import settings

class TournamentView:
    @staticmethod
    def display_tournament(tournament):
        """Affiche les informations d'un tournoi."""
        print(f"Tournoi : {tournament.name}")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de tours : {tournament.total_rounds}")
        print(f"Joueurs inscrits : {len(tournament.participants)}")

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche une liste de tournois."""
        for tournament in tournaments:
            print('-' * 20)
            TournamentView.display_tournament(tournament)

    @staticmethod
    def prompt_for_tournament_details():
        """Demande à l'utilisateur d'entrer les détails d'un tournoi."""
        from controllers.tournament_controller import TournamentController
        while True:
            name = input("Nom du tournoi : ")
            if not settings.check_empty(name):
                break
        while True:
            location = input("Lieu du tournoi : ")
            if not settings.check_empty(location):
                break
        while True:
            while True:
                start_date = input("Date de début (JJ-MM-AAAA) : ")
                if not settings.check_empty(start_date):
                    if settings.check_date(start_date):
                        break
            while True:
                end_date = input("Date de fin (JJ-MM-AAAA) : ")
                if not settings.check_empty(end_date):
                    if settings.check_date(end_date):
                        break
            if TournamentController.compare_dates(start_date, end_date):
                break
        while True:
            description = input("Description : ")
            if not settings.check_empty(description):
                break
        return name, location, start_date, end_date, description
    
    @staticmethod
    def prompt_to_find_tournament(tournament_controller):
        """Demande à l'utilisateur le nom d'un tournoi"""
        while True:
            while True:
                tournament_name = input("Nom du tournoi : ")
                if not settings.check_empty(tournament_name):
                    break
            while True:
                tournament_date = input("Date du tournoi : ")
                if not settings.check_empty(tournament_date):
                    break
            if tournament_controller.check_tournament_exists(tournament_name, tournament_date, error = False):
                break

        return tournament_name, tournament_date