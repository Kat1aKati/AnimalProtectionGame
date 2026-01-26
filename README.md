# AnimalProtectionGame / SAVE THE ANIMALS

This game is about saving animals.

[![status](https://img.shields.io/badge/status-work%20in%20progress-orange)](https://github.com/Kat1aKati/AnimalProtectionGame)

## Table of contents

- [About](#about)
- [How to install](#installation)
- [Contact owners!](#contacts)

## About
- when someone ask you: "are you animal saver?" they thinks you're saving cats dogs and other "basic" animals. but you will never realised in this game you will saving cows! yes.. cows... but! if you'[...]

## Installation

Below are clear, cross-platform instructions to set up and run this project locally. Replace the repository URL with a fork or your clone if needed.

1) Prerequisites
- Git installed: git --version
- Python 3.8+ installed (I recommend 3.10+): python --version or python3 --version
- pip available: python -m pip --version

2) Clone the repository
```bash
git clone https://github.com/Kat1aKati/AnimalProtectionGame.git
cd AnimalProtectionGame
```

3) Create and activate a virtual environment
- macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, run (as user):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- Windows (cmd):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

4) Upgrade pip (recommended)
```bash
python -m pip install --upgrade pip
```

5) Install dependencies
- If the repository contains requirements.txt:
```bash
pip install -r requirements.txt
```
- If there is no requirements.txt, a common dependency for simple Python games is pygame:
```bash
pip install pygame
```
(Replace or add any specific packages the project requires.)

6) Run the game
Try the common entry points:
```bash
python main.py
python app.py
python run.py
```
If none of those exist, look for a package with an __main__.py or a README note. You can list Python files to find possible entry points:
```bash
ls -1 *.py
```
If the project is a package (folder with __init__.py) you can run:
```bash
python -m packagename
```

7) When finished
```bash
deactivate
```

Troubleshooting
- If python refers to Python 2 on your system use python3 (and python3 -m venv).
- Activate the .venv before pip installing to avoid permission issues.
- If pip fails building a package, paste the error here and I can help.

## Contacts
Katia — katia.kati1221@gmail.com
