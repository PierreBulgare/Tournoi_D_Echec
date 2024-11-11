# Application de Gestion de Tournoi d'Échecs

## Informations sur la version
**Version** : 1.0.0  
**Date** : 10/11/2024 
**Auteur** : Pierre BULGARE

## Description
Ce programme permet de gérer des tournois d'échecs en toute autonomie, même hors ligne. L'outil offre une interface simple pour organiser des tournois, gérer les joueurs, enregistrer les résultats des matchs, et produire des classements. Le logiciel utilise le format JSON pour stocker les données, ce qui facilite la sauvegarde et la réutilisation des résultats de tournois passés. Il est aussi possible de générer les données enregistrés au format txt ou html pour une meilleure lecture.

## Prérequis
- **Python 3.7 ou une version supérieure** : [Téléchargements](https://www.python.org/downloads/).
- **flake8** `7.1.1`
- **flake8-html** `0.4.3`

_Si Python est déjà installé sur votre système, vous pouvez vérifier la version en tapant dans votre terminal : `python --version` pour Windows et `python3 --version` pour Mac OS/Linux._

## Mode d'emploi
### Installation de l'environnement Python virtuel
Pour utiliser le programme, vous devez d'abord installer un environnement Python et installer les prérequis :

**Windows**
- Lancez le fichier `launch.bat`

**Mac OS/Linux**
- Lancez le fichier `launch.sh`

_Ce fichier vérifiera si Python et Pip sont installés sur votre système, puis créera un environnement virtuel s'il n'existe pas déjà. Ensuite, il s'assurera que les packages requis sont installés dans cet environnement et les installera automatiquement si nécessaire. Enfin, il exécutera le programme via script `main.py`._

---

## Menu du Programme

1. Ajouter un joueur 

_(Ajoute un fichier `json` dans le répertoire `data/players` ex: AB12345.json contenant l'INE, le nom, le prénom et la date de naissance du joueur.)_

2. Créer un tournoi 

_(Ajoute un fichier `json` dans le répertoire `data/tournaments` ex: Tournoi_de_Paris-01-11-2024.json contenant le nom du tournoi, la description, le lieu, la date de début et de fin, le nombre de tours, le numéro du tour actuel, la liste des participants et la liste des tours.)_

3. Ajouter un joueur à un tournoi

_(Ajoute un joueur disponible dans la liste des joueurs présent dans les fichiers json de `data/players` à un tournoi présent dans `data/tournaments` à partir de leur INE puis sauvegarde le fichier json du tournoi.)_

4. Ajouter plusieurs joueurs à un tournoi

_(Ajoute en une fois, plusieurs joueurs à un tournoi en séparant leur INE par une virgule.)_

5. Ajouter un tour à un tournoi

_(Ajoute un tour à un tournoi en sélectionnant de manière aléatoire les joueurs pour le premier tour puis en fonction de leur score pour les tours suivants.)_

6. Terminer un tour

_(Marque un tour comme terminé puis mets à jours les scores dans les fichiers json des joueurs concernés ainsi que dans le fichier json du tournoi.)_

***Affichage dans le Terminal***

7. Afficher la liste des joueurs

_(Affiche la liste des joueurs de la base de donnée `data/players` dans le Terminal.)_

8. Afficher la liste des tournois

_(Affiche la liste des tournois de la base de donnée `data/tournaments` dans le Terminal.)_

***Génération de rapports (TXT/HTML)***

9. Générer la liste de tous les joueurs

_(Génère la liste de tous les joueurs dans un fichier TXT et un fichier HTML dans le répertoire `reports`.)_

10. Générer la liste des tournois

_(Génère la liste de tous les tournois dans un fichier TXT et un fichier HTML dans le répertoire `reports`.)_

11. Générer les données d'un tournoi

_(Génère les données d'un tournoi (Lieu/Dates/) dans un fichier TXT et un fichier HTML dans le répertoire `reports`.)_

12. Générer la liste des joueurs d'un tournoi

_(Génère la liste des joueurs d'un tournoi dans un fichier TXT et un fichier HTML dans le répertoire `reports`.)_

13. Générer la liste des tours et matchs d'un tournoi

_(Génère la liste des tours et matchs d'un tournoi dans un fichier TXT et un fichier HTML dans le répertoire `reports`.)_

***Quitter le Programme***

0. Quitter

_(Arrête le programme)_

---

# Rapport Flake8
Pour générer un rapport flake8, lancez la commande suivante dans le terminal depuis la racine du projet:

```
flake8 --format=html --htmldir=flake8_report
```

---

Si vous ne pouvez pas utiliser les fichiers de lancement `launch.bat` ou `launch.sh`, vous pouvez installer manuellement l'environnement Python et les prérequis en exécutant les commandes suivantes dans votre terminal :

_Vérifiez que vous êtes bien dans le répertoire où se trouvent `requirements.txt` et `main.py` avant de lancer les commandes ci-dessous._

**Windows**
1. Créez l'environnement virtuel : `python -m venv venv`
2. Activez l'environnement : `venv\Scripts\activate`
3. Installez les prérequis : `pip install -r requirements.txt`
4. Exécutez le programme : `python main.py`

**Mac OS/Linux**
1. Créez l'environnement virtuel : `python3 -m venv venv`
2. Activez l'environnement : `source venv/bin/activate`
3. Installez les prérequis : `pip3 install -r requirements.txt`
4. Exécutez le programme : `python3 main.py`