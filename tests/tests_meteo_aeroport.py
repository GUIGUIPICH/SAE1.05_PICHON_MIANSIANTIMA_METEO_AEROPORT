from scrapsite import *

def meteoaeroport(airportname):
    #Mise à jour du temps
    
    #Récupération des liens
    siteallmetsat=site_allmetsat(airportname)
    sitemeteoblue=site_meteoblue(airportname)
    
    #Mise à jour des variables pour aujourd'hui
    today = weathertoday(siteallmetsat)
    wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds = today
    
    #Mise à jour des variables pour Demain
    tomorrow = weatherforecast(1, sitemeteoblue)
    forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1 = tomorrow
    
    #Mise à jour des variables pour J+2
    d2 = weatherforecast(2, sitemeteoblue)
    forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2 = d2
    
    #Mise à jour des variables pour J+3
    d3 = weatherforecast(3, sitemeteoblue)
    forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3 = d3
    
    #Ajout des données sur le site internet
    update_website(wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds, forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1, forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2, forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3)
    