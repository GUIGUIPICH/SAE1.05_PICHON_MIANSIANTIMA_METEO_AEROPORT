# Météo d'un aéroport - SAE 1.05 - Traiter des données

## Objectif du projet

L’objectif principal de cette SAÉ est de vous confronter à une problématique professionnelle que vous serez amenés à rencontrer en tant que technicien R&T. Ce problème devra être résolu à l’aide d’un programme ou d’un ensemble de programmes et sera pour vous l’occasion de réaliser votre premier projet de développement informatique R&T.

## Description du projet

Ce programme a pour but de récupérer les données météo actuelles ainsi que celles prévues pour les 3 prochains jours sur divers sites météo pour l'aéroport de votre choix, puis d'afficher ensuite les données essentielles sur un site web clair et agréable sans le superflux. 

## Données affichées

Voici les données affichées :
- Maintenant : Date et heure, Vitesse et direction du vent, Humidité, Température, Pression, Visibilité, Nuages.
- Pour les 3 prochains jours : Vitesse et direction du vent, Température maximale et minimale, Prévision météo, Taux de précipitation, Pression.
Les données sont actualisées toutes les 5 minutes

## Prérequis 

- Python 3.7 minimum
- Accès Internet

## Utilisation du programme

Avant de commencer l’installation, vérifier que Python 3.7 minimum est installé sur le PC, pour vérifier, ouvrir un terminal et taper la commande `python` sur Windows ou `python3` sur Linux, et que la connexion à Internet fonctionne correctement
1) Ouvrir un terminal à l’emplacement où vous souhaitez installer le projet.
2) Cloner ensuite le dépôt en utilisant la commande suivante : `git clone https://github.com/GUIGUIPICH/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT.git` 
3) Se placer vous ensuite dans le répertoire du projet : `cd SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT`
4) Lancer ensuite le programme en utilisant la commande suivante, en remplaçant [NOM_AEROPORT] par l’aéroport que vous souhaitez utiliser.
Windows: `python meteo_aeroport/meteo_aeroport.py –aeroport [NOM_AEROPORT] --output-dir ./../html`
Linux: `python3 meteo_aeroport/meteo_aeroport.py –aeroport [NOM_AEROPORT] --output-dir ./../html`
5) Les données sont accessibles ensuite dans le fichier html/index.html de l’arborescence. L'accès est également possible en tapant `https://[REP_PROJET]/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT.git/html/index.html` dans votre navigateur (en remplaçant [REP_PROJET] par le dossier où vous avez placé l’arborescence).

Le projet est maintenant installé ! Les données météorologiques pour ce jour et les jours suivants sont affichées sur la page HTML. 


## Structure du Projet / Arborescence

Vous trouverez dans le projet la structure suivante :

`meteo_aerport/` : Dossier contenant le programme principal.
- `meteo_aeroport.py`: Script principal permettant d'exécuter le programme.
- `module_meteo_aeroport.py`: Module contenant les fonctions du programme.

`tests/` : Dossier contenant les tests unitaires du programme.
- `test_meteo_aeroport.py`: Fichier de tests unitaires pour les fonctions du module.
  
`html/` : Dossier contenant la page web contenant les données finales du programme.
- `index.html` : Fichier HTML contenant les données.
- `CSS/` : Fichier contenant les feuilles de style pour la page HTML.
- `images/` : Contient les images du site web.
  
`docs/` : Dossier contenant la documentation Sphynx du programme

## Documentation

Une documentation complète réalisée à l'aide du logiciel Sphinx. Celle ci est disponible dans le dossier docs/. Vous y trouverez une documentation du projet ainsi qu'un rappel du cahier des charges de celui ci, et d'autres informatio

## Prérequis

- Python 3.7 minimum
- Accès Internet

## Auteurs

- [Guillaume PICHON (GUIGUIPICH)](mailto:guillaume.pichon@etu.univ-poitiers.fr)
- [Promisse MIANSIANTIMA (PromisseLord)](mailto:promisse.miansiantima@etu.univ-poitiers.fr)
  
---
