import requests
from bs4 import BeautifulSoup
import re

def site_allmetsat(airport_name):
    '''
    Cherche le lien des données météo de l'aéroport sur le site Allmetsat
    Parameters
    −−−−−−−−−−−
    airport_name : nom de l'aéroport ou de la ville
    
    pre: airport_name de type char
    
    Returns
    −−−−−−−
    site_allmetsat1 : Lien météo du site Allmetsat
    
    Examples
    −−−−−−−−
    >>> weathertoday(poitiers)
    Out[8]: ('https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI')
    '''
    query=f"{airport_name} site:allmetsat.com"
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()    

        soup = BeautifulSoup(response.text, 'html.parser')
        site_allmetsat1 = soup.find('div', {'class': 'tF2Cxc'}).find('a')['href']

        return site_allmetsat1

    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
        return None
    
def site_meteoblue(airport_name):
    '''
    Cherche le lien des données météo de l'aéroport sur le site Météoblue
    Parameters
    −−−−−−−−−−−
    airport_name : nom de l'aéroport ou de la ville
    
    pre: airport_name de type char
    
    Returns
    −−−−−−−
    site_meteoblue1 : Lien météo du site météoblue
    
    Examples
    −−−−−−−−
    >>> weathertoday(poitiers)
    Out[8]: ('https://www.meteoblue.com/fr/meteo/semaine/poitiers_france_2986495')
    '''
    query=f"{airport_name} site:meteoblue.com"
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()    

        soup = BeautifulSoup(response.text, 'html.parser')
        site_meteoblue1 = soup.find('div', {'class': 'tF2Cxc'}).find('a')['href']

        return site_meteoblue1

    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
        return None


def weathertoday(site_allmetsat1):
    '''
    Cherche les données météorologiques sur le site Allmetsat
    Parameters
    −−−−−−−−−−−
    site_airport_allmetsat : Lien de la météo de l'aéroport sur le site Allmetsat
    
    pre: site_allmetsat1 de type char
    
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
    >>> weathertoday(https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI)
    Out[8]: ('11', 'sud-ouest', '13', '94', '1009', '10 km ou plus', 'Inconnu')
    '''
    url = site_allmetsat1
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


def weatherforecast(k, site_meteoblue1):
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
    url = f"{site_meteoblue1}?day={k}" #1 = aujourd'hui
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = response.text
        
        start_tag = soup.find('div', id=f'day{k}')
        content1 = start_tag.find_next('div', class_='tab-content')

        forecast = content1.find('img')['alt']
        temp_max = content1.find('div', class_='tab-temp-max').get_text(strip=True)
        temp_min = content1.find('div', class_='tab-temp-min').get_text(strip=True)
        wind_speed = content1.find('div', class_='wind').get_text(strip=True)
        wind_direction = content1.find('div', class_='wind').find('span')['class'][2]
        precipitation = content1.find('div', class_='tab-precip').get_text(strip=True)
        
        content2 = soup.find('div', class_='misc')
        pressure = content2.find('span', class_='value').get_text(strip=True)
        
        if wind_direction == "S":
            wind_direction = "Sud"
        elif wind_direction == "SW":
            wind_direction = "Sud-Ouest"
        elif wind_direction == "W":
            wind_direction = "Ouest"
        elif wind_direction == "NW":
            wind_direction = "Nord-Ouest"
        elif wind_direction == "N":
            wind_direction = "Nord"
        elif wind_direction == "NE":
            wind_direction = "Nord-Est"
        elif wind_direction == "E":
            wind_direction = "Est"
        elif wind_direction == "SE":
            wind_direction = "Sud-Est"
    
    return forecast, temp_max, temp_min, wind_speed, wind_direction, precipitation, pressure

def update_website(wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds,  forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1, forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2, forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3):
    f = open("../html/index.html",'w',encoding='utf-8')
    HTML_INDEX = f""" <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Météo Aéroport</title>
            <link rel="stylesheet" href="CSS/style.css" type="text/css" />
        </head>
        <body>
            <header>
                <h1>Météo Aéroport - Poitiers - Biard</h1>
                <h2>Poitiers - Biard</h2>
                <h3>[DATE - HEURE]</h3>
            </header>
            <article>
            <div class="container">
                <h2>Maintenant</h2>
                <p>Mise à jour :</p>
                <p>Vent : {wind_speed} km/h</p>
                <p>Orientation du vent : {wind_direction}</p>
                <p>Humidité : {humidity}%</p>
                <p>Température : {temperature}°C</p>
                <p>Pression : {pressure} hPa</p>
                <p>Visibilité : {visibility}</p>
                <p>Nuages : {clouds}</p>
                <p>Source des données : <a href"https://allmetsat.com">Allmetsat</a></p>
            </div>
    
            <div class="container">
                <h2>Demain</h2>
                <p>Prévision : {forecast1}</p>
                <p>Vent : {wind_speed1}</p>
                <p>Orientation du vent : {wind_direction1}</p>
                <p>Température maximale : {temp_max1}</p>
                <p>Température minimale : {temp_min1}</p>
                <p>Précipitations : {precipitation1}</p>
                <p>Pression : {pressure1}</p>
                <p>Source des données : <a href"https://meteoblue.com">Meteoblue</a></p>
    
            <div class="container">
                <h2>Demain</h2>
                <p>Prévision : {forecast2}</p>
                <p>Vent : {wind_speed2}</p>
                <p>Orientation du vent : {wind_direction2}</p>
                <p>Température maximale : {temp_max2}</p>
                <p>Température minimale : {temp_min2}</p>
                <p>Précipitations : {precipitation2}</p>
                <p>Pression : {pressure2}</p>
                <p>Source des données : <a href"https://meteoblue.com">Meteoblue</a></p>
                
            <div class="container">
                <h2>Demain</h2>
                <p>Prévision : {forecast3}</p>
                <p>Vent : {wind_speed3}</p>
                <p>Orientation du vent : {wind_direction3}</p>
                <p>Température maximale : {temp_max3}</p>
                <p>Température minimale : {temp_min3}</p>
                <p>Précipitations : {precipitation3}</p>
                <p>Pression : {pressure3}</p>
                <p>Source des données : <a href"https://meteoblue.com">Meteoblue</a></p>
            </div>
            </div>
        </article>
        </body>
    </html>
        """
    f.write(HTML_INDEX)





