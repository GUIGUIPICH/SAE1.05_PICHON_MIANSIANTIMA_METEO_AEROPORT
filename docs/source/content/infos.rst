.. test_sphinx documentation master file, created by
   sphinx-quickstart on Sat Dec  4 10:20:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Informations
************

Objectif du projet
==================

L’objectif principal de cette SAÉ est de vous confronter à une problématique professionnelle que vous serez amenés à rencontrer en tant que technicien R&T. Ce problème devra être résolu à l’aide d’un programme ou d’un ensemble de programmes et sera pour vous l’occasion de réaliser votre premier projet de développement informatique R&T.

Description du projet
=====================

Ce programme a pour but de récupérer les données météo actuelles ainsi que celles prévues pour les 3 prochains jours sur divers sites météo pour l'aéroport de votre choix, puis d'afficher ensuite les données essentielles sur un site web clair et agréable sans le superflux. 

Données affichées
=================

Voici les données affichées :
- Maintenant : Date et heure, Vitesse et direction du vent, Humidité, Température, Pression, Visibilité, Nuages.
- Pour les 3 prochains jours : Vitesse et direction du vent, Température maximale et minimale, Prévision météo, Taux de précipitation, Pression.

Prérequis 
=========

- Python 3.7 minimum
- Accès Internet

Utilisation du programme
========================

Avant de commencer l’installation, vérifier que Python 3.7 minimum est installé sur le PC, pour vérifier, ouvrir un terminal et taper la commande `python` sur Windows ou `python3` sur Linux, et que la connexion à Internet fonctionne correctement

1) Ouvrir un terminal à l’emplacement où vous souhaitez installer le projet.

2) Cloner ensuite le dépôt en utilisant la commande suivante : 
   
   .. code-block:: bash
       
       git clone https://github.com/GUIGUIPICH/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT.git

Vous pouvez également télécharger le projet au format ZIP : `https://github.com/GUIGUIPICH/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT/releases <https://github.com/GUIGUIPICH/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT/releases>`_.

3) Se placer ensuite dans le répertoire du projet : 

   .. code-block:: bash
       
       cd SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT
       
4) Installer les modules requis à l'aide de la commande suivante

   .. code-block:: bash
       
       pip install -r requirements.txt
       
5) Lancer ensuite le programme en utilisant la commande suivante, en remplaçant [NOM_AEROPORT] par l’aéroport que vous souhaitez utiliser.

   - Sous Windows : 

     .. code-block:: bash 
         
         python meteo_aeroport/meteo_aeroport.py –-aeroport [NOM_AEROPORT] --output-dir ./html

   - Sous Linux : 

     .. code-block:: bash
       
         python3 meteo_aeroport/meteo_aeroport.py –-aeroport [NOM_AEROPORT] --output-dir ./html


Note : L’aéroport doit être tapé en 1 seul mot. Dans le cas où celui-ci en prend plusieurs, remplacer les espaces par des underscore (« _ »). Pour éviter les erreurs sur le choix de l’aéroport, veuillez taper le plus précisément possible le nom de l’aéroport, et éviter les abréviations.

6) Les données sont accessibles ensuite dans le fichier html/index.html de l’arborescence. L'accès est également possible en tapant `https://[REP_PROJET]/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT.git/html/index.html` dans votre navigateur (en remplaçant [REP_PROJET] par le dossier où vous avez placé l’arborescence).


Le projet est maintenant installé ! Les données météorologiques pour ce jour et les jours suivants sont affichées sur la page HTML. 


Structure du Projet / Arborescence
==================================

Vous trouverez dans le projet la structure suivante :

.. code-block:: rst

    meteo_aerport/ : Dossier contenant le programme principal.
    - meteo_aeroport.py: Script principal permettant d'exécuter le programme.
    - module_meteo_aeroport.py: Module contenant les fonctions du programme.

    tests/ : Dossier contenant les tests unitaires du programme.
    - test_meteo_aeroport.py: Fichier de tests unitaires pour les fonctions du module.

    html/ : Dossier contenant la page web contenant les données finales du programme.
    - index.html : Fichier HTML contenant les données.
    - CSS/ : Fichier contenant les feuilles de style pour la page HTML.
    - images/ : Contient les images du site web.

    docs/ : Dossier contenant la documentation Sphinx du programme

	
Documentation
=============

Une documentation complète réalisée à l'aide du logiciel Sphinx. Celle ci est disponible dans le dossier docs/. Vous y trouverez une documentation du projet ainsi qu'un rappel du cahier des charges de celui ci, et d'autres informations.

Prérequis
=========

- Python 3.7 minimum
- Accès Internet
  

