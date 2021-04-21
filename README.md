# Exemple de structure pour un projet de scraping

Ce dépôt de code présente un exemple de structure pour organiser 
un projet de scraping.

## Installation des dépendances

Pour installer les dépendances de ce projet, il faut commencer par installer pipenv avec la commande `py -m pip install pipenv` (sous windows) ou `brew install pipenv` (sous macos) ou `python3 -m pip install --user pipenv` (sous Ubuntu ou Debian).

1. Création de l'environnement virtuel et installation des dépendances avec `pipenv install`.
2. Activation de l'environnement virtuel avec `pipenv shell`.
3. Démarrer un script avec par exemple `python -m bookstoscrape.books`