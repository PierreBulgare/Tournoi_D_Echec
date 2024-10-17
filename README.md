# Application de Gestion de Tournoi d'Échecs

## Informations sur la version
**Version** : 1.0.0  
**Date** : 17/10/2024 
**Auteur** : Pierre BULGARE

## Description
Ce programme permet de gérer des tournois d'échecs en toute autonomie, même hors ligne. L'outil offre une interface simple pour organiser des tournois, gérer les joueurs, enregistrer les résultats des matchs, et produire des classements. Le logiciel utilise le format JSON pour stocker les données, ce qui facilite la sauvegarde et la réutilisation des résultats de tournois passés.

## Prérequis
- **Python 3.7 ou une version supérieure** : [Téléchargements](https://www.python.org/downloads/).

_Si Python est déjà installé sur votre système, vous pouvez vérifier la version en tapant dans votre terminal : `python --version` pour Windows et `python3 --version` pour Mac OS/Linux._

## Mode d'emploi
### Installation de l'environnement Python virtuel
Pour utiliser le programme, vous devez d'abord installer un environnement Python et installer les prérequis :

**Windows**
- Lancez le fichier `launch.bat`

**Mac OS/Linux**
- Lancez le fichier `launch.sh`

Ce fichier vérifiera si Python et Pip sont installés sur votre système, puis créera un environnement virtuel s'il n'existe pas déjà. Ensuite, il s'assurera que les packages requis sont installés dans cet environnement et les installera automatiquement si nécessaire. Enfin, il exécutera le script `main.py`. ***

---

*** Si vous ne pouvez pas utiliser les fichiers de lancement `launch.bat` ou `launch.sh`, vous pouvez installer manuellement l'environnement Python et les prérequis en exécutant les commandes suivantes dans votre terminal :

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