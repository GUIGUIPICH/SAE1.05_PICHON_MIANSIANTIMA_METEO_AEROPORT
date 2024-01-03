from module_meteo_aeroport import *
import sys
import time

def main():
    #Vérification du nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: nom_projet.py --aeroport nom_aeroport --output-dir ../html/  \nAttention : Le nom de l'aéroport doit être écrit en un seul mot, Remplacez les espaces par des underscore le cas échéant")
        return
    
    #Récupération des arguments
    if sys.argv[1] == '--aeroport' and sys.argv[3] == '--output-dir':
        airportname = sys.argv[2]
        output_dir = sys.argv[4]
        
    print("Si l'aéroport affiché est incorrect, relancez le programme en écrivant plus précisément l'aéroport (Ex : Lyon St Exupéry au lieu de Lyon) ou en évitant les abréviations (Ex : Charles de Gaulle au lieu de CDG")
    print(f"Programme en cours de fonctionnement, Ctrl+C pour arrêter")
    
    compteur = 0
    while True:
        if compteur % 300 == 0:  # 300 secondes équivalent à 5 minutes
            #Récupération des liens
            siteallmetsat=site_allmetsat(airportname)
            sitemeteoblue=site_meteoblue(airportname)
            
            #Mise à jour des variables pour aujourd'hui
            today = weathertoday(siteallmetsat)
            airportname_complete, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds = today
            
            #Mise à jour des variables pour Demain
            tomorrow = weatherforecast(1, sitemeteoblue)
            forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1 = tomorrow
            
            #Mise à jour des variables pour J+2
            d2 = weatherforecast(2, sitemeteoblue)
            forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2 = d2
            
            #Mise à jour des variables pour J+3
            d3 = weatherforecast(3, sitemeteoblue)
            forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3 = d3
        else:
            #Récupération de la date et de l'heure
            actualtime = time_1()
            
            #Ajout des données sur le site internet
            update_website(airportname_complete, actualtime, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds, forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1, forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2, forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3, output_dir)
        time.sleep(1)
        compteur += 1
    
if __name__ == '__main__':
    main()
