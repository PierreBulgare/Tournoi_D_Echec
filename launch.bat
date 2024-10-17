@echo off
REM Vérifie si Python est installé
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERREUR] Python n'est pas installé sur votre ordinateur. Veuillez installer Python.
    pause
    exit /b
)

REM Crée un environnement virtuel s'il n'existe pas
IF NOT EXIST "venv" (
    echo [INFO] Création de l'environnement virtuel...
    python -m venv venv
)

REM Active l'environnement virtuel
echo [INFO] Activation de l'environnement virtuel...
CALL venv\Scripts\activate

REM Vérifie si pip est installé dans l'environnement virtuel
pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERREUR] Pip n'est pas installé dans l'environnement virtuel.
    pause
    exit /b
)

REM Mise à jour de pip
echo [INFO] Mise à jour de pip...
pip install --upgrade pip >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERREUR] Echec de la mise à jour de pip.
    pause
    exit /b
)

REM Installe les packages requis à partir de requirements.txt
echo [INFO] Installation des packages depuis requirements.txt...
pip install -r requirements.txt >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERREUR] Echec de l'installation des packages depuis requirements.txt.
    pause
    exit /b
)

REM Vérifie si main.py existe avant de l'exécuter
IF NOT EXIST "main.py" (
    echo [ERREUR] Le fichier main.py est introuvable.
    pause
    exit /b
)

REM Lance le fichier main.py
echo [INFO] Lancement du programme...
python main.py

REM Pause
pause
