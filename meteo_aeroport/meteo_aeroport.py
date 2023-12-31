from module_meteo_aeroport import *

import sys
import time
import argparse

def main():
    """
    Script principal du projet

    Utilise argparse pour analyser les arguments en ligne de commandes puis appelle les différentes fonctions afin d'aboutir en la génération de la page web.

    :returns: Aucun
    :rtype: None
    """
    
    # Définir le parseur d'arguments
    parser = argparse.ArgumentParser(description='Affiche le nom de l\'aéroport et le répertoire de sortie.')

    # Ajouter les arguments
    parser.add_argument('--aeroport', required=True, help='Nom de l\'aéroport')
    parser.add_argument('--output-dir', required=True, help='Répertoire de sortie')

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    # Définition des variables
    airportname = args.aeroport
    output_dir = args.output_dir
        
    print(f"Programme en cours de fonctionnement, Ctrl+C pour arrêter")

    #Récupération des liens
    siteallmetsat=site_allmetsat(airportname)
    sitemeteoblue=site_meteoblue(airportname)
        
    #Mise à jour des variables pour aujourd'hui
    today = weathertoday(siteallmetsat)
    airportname_complete, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds = today
        
    #Mise à jour des variables pour Demain
    tomorrow = weatherforecast(2, sitemeteoblue)
    forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1 = tomorrow
            
    #Mise à jour des variables pour J+2
    d2 = weatherforecast(3, sitemeteoblue)
    forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2 = d2
        
    #Mise à jour des variables pour J+3
    d3 = weatherforecast(4, sitemeteoblue)
    forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3 = d3
    
    #Récupération de la date et de l'heure
    actualtime = time_1()
    
    #Ajout des données sur le site internet
    update_website(airportname_complete, actualtime, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds, forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1, forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2, forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3, output_dir, siteallmetsat, sitemeteoblue)
    
    print(f"Programme Terminé. Données disponibles dans {output_dir}")
    
if __name__ == '__main__':
    main()
