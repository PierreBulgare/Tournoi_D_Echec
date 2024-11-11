from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    # Menu du programme
    while True:
        print("\nMenu Principal:")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Ajouter un joueur à un tournoi")
        print("4. Ajouter plusieurs joueurs à un tournoi")
        print("5. Ajouter un tour à un tournoi")
        print("6. Terminer un tour")
        print("=== Affichage dans le Terminal ===")
        print("7. Afficher la liste des joueurs")
        print("8. Afficher la liste des tournois")
        print("=== Génération de rapports (TXT/HTML) ===")
        print("9. Générer la liste de tous les joueurs")
        print("10. Générer la liste des tournois")
        print("11. Générer les données d'un tournoi")
        print("12. Générer la liste des joueurs d'un tournoi")
        print("13. Générer la liste des tours et matchs d'un tournoi")
        print("0. Quitter")
        choice = input("Choisissez une option : ")

        # Ajouter un joueur
        if choice == '1':
            player_controller.add_player()
        # Créer un tournoi
        elif choice == '2':
            tournament_controller.create_tournament()
        # Ajouter un joueur à un tournoi
        elif choice == '3':
            tournament_controller.add_player_to_tournament(player_controller)
        # Ajouter plusieurs joueurs à un tournoi
        elif choice == '4':
            tournament_controller.add_multiple_players_to_tournament(player_controller)
        # Ajouter un tour à un tournoi
        elif choice == '5':
            tournament_controller.add_round_to_tournament()
        # Terminer le tour d'un tournoi
        elif choice == '6':
            tournament_controller.end_round()
        # Afficher la liste des joueurs
        elif choice == '7':
            player_controller.list_players()
        # Afficher la liste des tournois
        elif choice == '8':
            tournament_controller.list_tournaments()
        # Générer la liste des joueurs par ordre alphabétiques
        elif choice == '9':
            player_controller.generate_players_list_alphabetically()
        # Générer la liste des tournois
        elif choice == '10':
            tournament_controller.generate_tournaments_list()
        # Générer le lieu et les dates d'un tournoi
        elif choice == '11':
            tournament_controller.generate_tournament_datas()
        # Générer la liste des joueurs d'un tournoi
        elif choice == '12':
            tournament_controller.generate_tournament_players_alphabetically()
        # Générer la liste des tours et matchs d'un tournoi
        elif choice == '13':
            tournament_controller.generate_tournament_rounds_and_games()
        # Quitter le programme
        elif choice == '0':
            break
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == '__main__':
    main()
