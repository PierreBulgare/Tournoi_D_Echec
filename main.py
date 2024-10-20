from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    # Menu du programme
    while True:
        print("\nMenu Principal:")
        print("1. Ajouter un joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Créer un tournoi")
        print("4. Afficher la liste des tournois")
        print("5. Ajouter un joueur à un tournoi")
        print("6. Ajouter un tour à un tournoi")
        print("0. Quitter")
        choice = input("Choisissez une option : ")

        # Ajouter un joueur
        if choice == '1':
            player_controller.add_player()
        # Afficher la liste des joueurs
        elif choice == '2':
            player_controller.list_players()
        # Créer un tournoi
        elif choice == '3':
            tournament_controller.create_tournament()
        # Afficher la liste des tournois
        elif choice == '4':
            tournament_controller.list_tournaments()
        # Ajouter un joueur à un tournoi
        elif choice == '5':
            tournament_controller.add_player_to_tournament(player_controller)
        # Ajouter un tour à un tournoi
        elif choice == '6':
            tournament_controller.add_round_to_tournament()
        # Quitter le programme
        elif choice == '0':
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()