======================================================================
Cahier des charges
======================================================================

-------------------------
Cadre et objectif général
-------------------------

Le projet a pour objectif d'extraire des données de sites web météo afin de pouvoir établir les prévisions météorologiques du jour et des quelques jours suivants.

  
Les étapes principales du projet consistent à :

 * lire et extraire les données pertinentes des fichiers html de sites web de météo ;
  
 * les traiter afin de pouvoir produire les données suivantes pour le jour J et pour quelques jours suivants :

    * Date et heure 
    * Direction du vent en degré
    * Vitesse du vent en km/h
    * La température en degré celsius
    * Le taux d'humidité en pourcentage
    * La pression atmosphérique en Pascal
    * La densité des nuages
    * La visibilité

 * de générer une page html/css sur laquelle seront présentées les données extraites et calculées.


Le projet doit :

* utiliser l'outil de gestion de version Git et un IDE de développement Python ;

* être structuré suivant l'arborescence indiquée ci-après

* pouvoir s'exécuter sur le système Linux des salle de TP lors de la démonstration finale ;

* être documenté :

        * description du projet au format restructuredText,
	* commentaires pertinents dans le code (si utile à la compréhension),
	* commentaires des fonctions développées


* comporter un répertoire de test où toutes les fonctions Python développées auront un code test unitaire

--------------------------------------------
Environnement de développement et dépôt GIT
--------------------------------------------

Le projet est rattaché à un dépôt GIT que vous aurez créé sur GitHub et à la livraison de vos codes informatiques. 
Le dépôt **devra absolument** être remis lors de la livraison finale du projet.
Le versionnement étant tracé et daté, il servira pour l'évaluation du travail.


-----------------------------------
Langages de scripting/programmation
-----------------------------------

Le projet doit utiliser :

* le langage de programmation **Python** (version > 3.7) pour les **codes sources** gérant la lecture, l'analyse, le traitement des données et la présentation des traitements. 

* et/ou le langage de script **bash** pour les scripts permettant l'automatisation de certains traitements et de la publication des résultats  (vu en **R108-Base des systèmes d'exploitation**)



----------------------
Arborescence du projet
----------------------


Votre projet doit :

* être exécuté par le biais d'un script ``nom_projet.py``. Ce script reprendra la structure classique des programmes vue en **R107-Fondamentaux de la programmation** et décrite dans le formulaire Python. Il prendra d'éventuels paramètres en arguments spécifiés ci-après. 

* respecter l'arborescence suivante (``PROJETGitHUB`` désigne le répertoire auquel est rattaché votre projet et constitue la base du dépôt local Git) :

   .. code-block:: bash

      PROJETGitHUB
      ├── .git/
      ├── data/
      │   └── ...
      ├── docs/
      │     ├── build/
      │     │    └── html/
      │     └── source/ 
      │    	 ├── index.rst 
      │    	 ├── conf.py 
      │    	 ├── content/ 
      │    	 ├── _static/ 
      │          └── _templates/    
      ├── html/
      │   └── ...
      ├── __init__.py
      ├── nomprojet/
      |    ├── nom_projet.py
      │    └── nom_module_projet.py
      ├── tests/
      │   ├── __init__.py
      │   └── test_nomprojet.py  
      ├── .gitignore
      ├── AUTHORS
      │ 
      └── requirements.txt


      
   * ``.git`` le répertoire dédié à Git.
  
   * ``data`` le répertoire dédié à stocker différents fichiers de données récupérées et générées pour les besoin du projet.

   * ``docs`` le répertoire dédié à stocker la documentation du projet au format retructuredText (répertoire généré automatiquement par sphinx-build).

   * ``html`` répertoire contenant le site web statique de présentation des résultats

   * ``__init__.py`` fichier indiquant la version du projet :
	.. code-block:: python
			
		__version__ = '0.1.0'

   * ``nomprojet`` le répertoire dédié aux fichiers source Python développés lors du projet

   * ``tests`` le répertoire dédié aux tests unitaires des fonctions développées dans le projet

   * ``tests/__init__.py`` fichier vide

   * ``.gitignore`` le fichier permettant de configurer Git pour ne pas envoyer sur le dépôt distant les fichiers temporaires 

   * ``AUTHORS`` le fichier indiquant le nom des auteurs et de leurs coordonnées 
          
   * ``requirements.txt`` fichier texte décrivant la version de Python  utilisée et les dépendances du programme python (modules et version des modules Python)
   

.. warning::

   * Les fichiers : ``.gitignore`` commence avec un point.

.. note:: Vous pouvez ajouter au besoin autant de modules que nécessaires, pour structurer votre code, en les stockant à la racine du répertoire ``nomprojet``.



---------------------------------------------
Paramètres en argument du programme principal
---------------------------------------------
Votre programme devra prendre en arguments le nom de l'aéroport et le répertoire dans lequel sera générée la page web :

 .. code-block:: bash
		 
	$ ./nom_projet.py --aeroport nom_aeroport --output-dir ./../html/

--------------------------------------------
Documentation
--------------------------------------------  
* La documentation générale du projet devra être écrite au format restructuredText. Vous pourrez pour cela vous appuyer sur le logiciel `Sphinx <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_ ;

* Il conviendra d'ajouter des commentaires *doctrings* en début de fonction afin de :

     * préciser ce que fait la fonction,
     * d'indiquer son auteur, ses dates de création et de dernière modification,
     * décrire ses paramètres et le cas échéant leurs types,
     * décrire les bornes d'utilisation de paramètres pour un bon fonctionnement de la fonction et exceptions qui sont suceptibles d'être levées,
     * ce qu'elle retourne
     * donner un exemple d'utilisation

--------------------
Tests unitaires
--------------------

En vous inspirant du TP sur les fonctions, vous devrez écrire un code de test de chaque fonction développée dans le projet.
Celui-ci sera placé dans un programme Python du répertoire ``tests``.





