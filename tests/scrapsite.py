import requests
from bs4 import BeautifulSoup
import re
from google import search

# airport_name="poitiers"

# def websites_links(airport_name) :
#     query=f"{airport_name} site:allmetsat.com",
#     def google_search(query, num_results=1):
#         try:
#             search_results = search(query, num_results=num_results, stop=num_results)
#             for result in search_results:
#                 return result
#         except Exception as e:
#             print(f"Une erreur s'est produite : {e}")
#     site_airport_allmetsat = google_search(query)
#     query=f"{airport_name} site:meteoblue.com"
#     def google_search(query, num_results=1):
#         try:
#             search_results = search(query, num_results=num_results, stop=num_results)
#             for result in search_results:
#                 return result
#         except Exception as e:
#             print(f"Une erreur s'est produite : {e}")
#     site_airport_meteoblue = google_search(query)
#     return site_airport_allmetsat, site_airport_meteoblue


def weathertoday(site_airport_allmetsat):
    '''
    Cherche les données météorologiques sur le site Allmetsat
    Parameters
    −−−−−−−−−−−
    site_airport_allmetsat : Lien de la météo de l'aéroport sur le site Allmetsat
    
    pre: site_airport_allmetsat de type char
    
    Returns
    −−−−−−−
    Toutes les valeurs sont sans les unités
    wind_speed : vitesse du vent en km/h
    wind_direction : direction du vent
    temperature : Température en °C
    humidity : Taux d'humidité en %
    pressure : Pression en Hpa
    visibility : Visibilité (avec l'unité)
    clouds : Densité des nuages
    
    Examples
    −−−−−−−−
    >>> weathertoday(https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI, https://www.meteoblue.com/fr/meteo/semaine/poitiers_france_2986495)
    Out[8]: ('11', 'sud-ouest', '13', '94', '1009', '10 km ou plus', 'Inconnu')
    '''
    url = "https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = response.text
        
        c1b_div = soup.find('div', class_='c1b')
        c1b_content = str(c1b_div)
        
        wind_speed = re.search(r"Vent\s*<b>([^<]+)</b>", c1b_content)
        wind_direction = re.search(r"Vent\s*<b>\d+</b>\s*kt de <b>([^<]+)</b>", c1b_content)
        temperature = re.search(r"Température\s*<b>([^<]+)</b>", c1b_content)
        humidity = re.search(r"Humidité\s*<b>([^<]+)</b>", c1b_content)
        pressure = re.search(r"Pression\s*<b>([^<]+)</b>", c1b_content)
        visibility = re.search(r"Visibilité\s*([^<]+)</div>", c1b_content)
        clouds = re.search(r"Nuages\s*<b>([^<]+)</b>", c1b_content)
        
        print("Maintenant \n")
        
        if wind_speed:
            wind_speed=wind_speed.group(1)
        else:
            wind_speed="Inconnu"
        if wind_direction:
            wind_direction=wind_direction.group(1)
        else:
            wind_direction="Inconnu"
        if temperature:
            temperature=temperature.group(1)
        else:
            temperature="Inconnu"
        if humidity:
            humidity=humidity.group(1)
        else:
            humidity="Inconnu"
        if pressure:
            pressure=pressure.group(1)
        else:
            pressure="Inconnu"
        if visibility:
            visibility=visibility.group(1)
        else :
            visibility="Inconnu"
        if clouds:
            clouds=clouds.group(1)
        else:
            clouds="Inconnu"
    return wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds


def weatherforecast(k, site_airport_meteoblue):
    '''
    Cherche les données météorologiques sur le site Meteoblue
    Parameters
    −−−−−−−−−−−
    site_airport_meteoblue : Lien de la météo de l'aéroport sur le site meteoblue
    k numéro du jour (à partir de celui ci dont l'on souhaite récupérer les infos)
    
    pre: site_airport_meteoblue de type char
    k de type int
    
    Returns
    −−−−−−−
    Toutes les valeurs sont avec les unités (char)
    wind_speed : vitesse du vent en km/h
    wind_direction : direction du vent
    temperature_max : Température maximale de la journée en °C
    temperature_min : Température minimale de la journée en °C
    precipitation : Taux de précipitation en mm
    pressure : Pression en Hpa
    
    Examples
    −−−−−−−−

    '''
    url = f"https://www.meteoblue.com/fr/meteo/semaine/poitiers_france_2986495?day={k}" #1 = aujourd'hui
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = response.text

        content1 = soup.find('div', class_='tab-content')

        forecast = content1.find('img')['alt']
        temp_max = content1.find('div', class_='tab-temp-max').get_text(strip=True)
        temp_min = content1.find('div', class_='tab-temp-min').get_text(strip=True)
        wind_speed = content1.find('div', class_='wind').get_text(strip=True)
        wind_direction = content1.find('div', class_='wind').find('span')['class'][1]
        precipitation = content1.find('div', class_='tab-precip').get_text(strip=True)
        
        content2 = soup.find('div', class_='misc')
        pressure = content2.find('span', class_='value').get_text(strip=True)
        
        print(f"Prévision: {forecast}")
        print(f"Température maximale: {temp_max}")
        print(f"Température minimale: {temp_min}")
        print(f"Vitesse du vent: {wind_speed}")
        print(f"Direction du vent: {wind_direction}")
        print(f"Quantité de précipitations: {precipitation}")
        print(f"Pression: {pressure}")
    
    return forecast, temp_max, temp_min, wind_speed, wind_direction, precipitation





