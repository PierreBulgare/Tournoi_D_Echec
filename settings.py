def format_file_name(file_name) -> str:
    return file_name.replace(" ", "_").replace("'", "_")


def check_empty(text: str) -> bool:
    if len(text) == 0:
        print("Erreur ! Ce champ ne peut pas être vide.")
        return True
    return False


def check_date(date: str) -> bool:
    # Vérifie si la date est bien au format JJ-MM-AAAA (Ex: 10-10-2024)
    if date[2] == "-" and date[5] == "-":
        # Vérifie si le jour est numérique et se situe entre 1 et 31
        if date[:2].isdigit() and 1 <= int(date[:2]) <= 31:
            # Vérifie si le mois est numérique et se situe entre 1 et 12
            if date[3:5].isdigit() and 1 <= int(date[3:5]) <= 12:
                # Vérifie si l'année est numérique et est bien au format AAAA (Ex: 2024)
                if date[6:].isdigit() and len(date[6:]) == 4:
                    return True
                else:
                    print("Erreur ! L'année doit être au format AAAA (Ex: 2024)")
                    return False
            else:
                print("Erreur ! Le mois doit se situer entre 1 et 12.")
                return False
        else:
            print("Erreur ! Le jour doit se situer entre 1 et 31.")
            return False
    else:
        print("Erreur ! Le format de la date doit être au format JJ-MM-AAAA (Ex: 10-10-2024)")
        return False
