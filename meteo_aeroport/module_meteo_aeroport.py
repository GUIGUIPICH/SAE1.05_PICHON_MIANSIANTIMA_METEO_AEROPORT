import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

"""
.. module:: module_meteo_aeroport
   :platform: Unix
   :synopsis: module pour extraire les données d'un site web

.. moduleauthor:: Guillaume PICHON <guillaume.pichon@etu.univ-poitiers.fr> Promisse MIANSIANTIMA <promisse.miansiantima@etu.univ-poitiers.fr>

"""

def site_allmetsat(airport_name):
    """
    Cette fonction permet de récupérer le lien météo du site Allmetsat

    :param param1: Nom de l'aéroport
    :type param1: str
    :returns: Lien Allmetsat de l'aéroport demandé
    :rtype: str
    :raises: TypeError
    :example:
    
    .. code-block:: python

    >>> weathertoday(poitiers)
    Out[8]: ('https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI')

    """
    query=f"{airport_name} site:allmetsat.com"
    try:
        #Effectue une recherche Google avec le nom de l'aéroport avec uniquement les résultats sur le site Allmetsat
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()    
        
        #Récupère le premier résultat
        soup = BeautifulSoup(response.text, 'html.parser')
        site_allmetsat1 = soup.find('div', {'class': 'tF2Cxc'}).find('a')['href']

        return site_allmetsat1
    except Exception as e:
        #Affiche une erreur en cas de problème (erreur de connexion..)
        print(f"Erreur lors de la recherche : {e}")
        return None
    
def site_meteoblue(airport_name):
    """ 
    Cette fonction permet de récupérer le lien météo du site Allmetsat

    :param param1: Nom de l'aéroport
    :type param1: str
    :returns: Lien Meteoblue de l'aéroport demandé
    :rtype: str
    :raises: TypeError
    :example:
    
    .. code-block:: python

    >>> weathertoday(poitiers)
    Out[8]: ('https://www.meteoblue.com/fr/meteo/semaine/poitiers_france_2986495')
    """
    query=f"{airport_name} meteo semaine site:meteoblue.com"
    try:
        #Effectue une recherche Google avec le nom de l'aéroport avec uniquement les résultats sur le site Allmetsat
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()    
        
        #Récupère le premier résultat
        soup = BeautifulSoup(response.text, 'html.parser')
        site_meteoblue1 = soup.find('div', {'class': 'tF2Cxc'}).find('a')['href']

        return site_meteoblue1

    except Exception as e:
        #Affiche une erreur en cas de problème (erreur de connexion..)
        print(f"Erreur lors de la recherche : {e}")
        return None


def weathertoday(site_allmetsat1):
    """ 
    Cette fonction permet de récupérer les données météo sur le site Allmetsat pour l'instant actuel

    :param param1: Lien du site météo Allmetsat de l'aéroport
    :type param1: str
    :returns: Nom complet et données météorologiques de l'aéroport pour l'instant actuel
    :rtype: list
    :raises: TypeError
    :example:
    
    .. code-block:: python

    >>> weathertoday("https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI"")
    Out[8]: ('Aéroport de Poitiers-Biard', '11', 'sud-ouest', '13', '94', '1009', '10 km ou plus', 'Inconnu')
    """
    #Effectue une requête vers le site Allmetsat pour récupérer les données
    url = site_allmetsat1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200: #si la requête a abouti
        soup = BeautifulSoup(response.text, 'html.parser')
        content = response.text
        
        #Indique à quel endroit de la page chercher les données
        c1b_div = soup.find('div', class_='c1b')
        c1b_content = str(c1b_div)
        
        #Cherche ensuite les données que l'on souhaite obtenir      
        airportname_complete = c1b_div.find('h1')
        wind_speed = re.search(r"Vent\s*<b>([^<]+)</b>", c1b_content)
        wind_direction = re.search(r"Vent\s*<b>\d+</b>\s*kt de <b>([^<]+)</b>", c1b_content)
        temperature = re.search(r"Température\s*<b>([^<]+)</b>", c1b_content)
        humidity = re.search(r"Humidité\s*<b>([^<]+)</b>", c1b_content)
        pressure = re.search(r"Pression\s*<b>([^<]+)</b>", c1b_content)
        visibility = re.search(r"Visibilité\s*(.+?)\s*</div>", c1b_content)
        clouds = re.search(r"Nuages\s*<b>([^<]+)</b>", c1b_content)
        
        # Place "Inconnu" dans le cas où les données sont introuvables, et verifie que ces valeurs sont bien de type str
        if wind_speed:
            wind_speed = wind_speed.group(1)
            wind_speed = float(wind_speed)
            wind_speed_kph = wind_speed * 1.852  # Conversion en kilomètres par heure
            wind_speed_kph = round(wind_speed_kph, 2)
            wind_speed = str(wind_speed_kph)
        else:
            wind_speed = "Inconnu"
        assert isinstance(wind_speed, str)
    
        if wind_direction:
            wind_direction = wind_direction.group(1)
        else:
            wind_direction = "Inconnu"
        assert isinstance(wind_direction, str)
    
        if temperature:
            temperature = temperature.group(1)
        else:
            temperature = "Inconnu"
        assert isinstance(temperature, str)
    
        if humidity:
            humidity = humidity.group(1)
        else:
            humidity = "Inconnu"
        assert isinstance(humidity, str)
    
        if pressure:
            pressure = pressure.group(1)
        else:
            pressure = "Inconnu"
        assert isinstance(pressure, str)
    
        if visibility:
            visibility = visibility.group(1)
            visibility = re.sub(r'<b>(.*?)</b>', r'\1', visibility)
        else:
            visibility = "Inconnu"
        assert isinstance(visibility, str)
    
        if clouds:
            clouds = clouds.group(1)
        else:
            clouds = "Inconnu"
        assert isinstance(clouds, str)
    return airportname_complete, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds


def weatherforecast(k, site_meteoblue1):
    """ 
    Cette fonction permet de récupérer la météo sur le site Météoblue pour le jour donné

    :param param1: Jour souhaité pour la récupération météo
    :type param1: int
    :param param2: Lien du site météo Meteoblue de l'aéroport
    :type param2: str
    :returns: Données météorologiques de l'aéroport pour le jour demandé
    :rtype: list
    :raises: TypeError
    :example:
    
    .. code-block:: python

    >>> weatherforecast(2, "https://www.meteoblue.com/fr/meteo/semaine/poitiers_france_2986495")
    Out[9]: ('Couvert avec pluie', '12\xa0°C','8\xa0°C', '44-79','Sud-Ouest', '5-10 mm', '1007 hPa')
    
    """
    #Effectue une requête sur le site Meteoblue pour récupérer les données d'un jour donné
    url = f"{site_meteoblue1}?day={k}" #1 = aujourd'hui
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = response.text
        
        #Indique à partir de quel endroit les données doivent être cherchées
        start_tag = soup.find('div', id=f'day{k}')
        content1 = start_tag.find_next('div', class_='tab-content')

        #Cherche ensuite les données que l'on veut obtenir
        forecast = content1.find('img')['alt']
        temp_max = content1.find('div', class_='tab-temp-max').get_text(strip=True)
        temp_min = content1.find('div', class_='tab-temp-min').get_text(strip=True)
        wind_speed = content1.find('div', class_='wind').get_text(strip=True)
        wind_direction = content1.find('div', class_='wind').find('span')['class'][2]
        precipitation = content1.find('div', class_='tab-precip').get_text(strip=True)
        
        #Cherche la pression qui est affichée en bas de la page        
        content2 = soup.find('div', class_='misc')
        pressure = content2.find('span', class_='value').get_text(strip=True)
        
        #Changement de format de la direction du vent pour une meilleur lisibilité
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
            
        #Assertions pour vérifier le type des valeurs retournées
        assert isinstance(forecast, str), f"La valeur de 'forecast' n'est pas de type str: {type(forecast)}"
        assert isinstance(temp_max, str), f"La valeur de 'temp_max' n'est pas de type str: {type(temp_max)}"
        assert isinstance(temp_min, str), f"La valeur de 'temp_min' n'est pas de type str: {type(temp_min)}"
        assert isinstance(wind_speed, str), f"La valeur de 'wind_speed' n'est pas de type str: {type(wind_speed)}"
        assert isinstance(wind_direction, str), f"La valeur de 'wind_direction' n'est pas de type str: {type(wind_direction)}"
        assert isinstance(precipitation, str), f"La valeur de 'precipitation' n'est pas de type str: {type(precipitation)}"
        assert isinstance(pressure, str), f"La valeur de 'pressure' n'est pas de type str: {type(pressure)}"
    
    return forecast, temp_max, temp_min, wind_speed, wind_direction, precipitation, pressure

def time_1():
    """ 
    Cette fonction permet de récupérer la date et l'heure

    :param param1: Aucun
    :returns: Date et heure actuelles dans un format lisible
    :rtype: str
    :raises: TypeError
    :example:
    
    .. code-block:: python
    Out[10]: '03-01-2024 13:14'

    >>> time_1()
    
    """
    time_actual_unformated = datetime.now()
    actualtime = time_actual_unformated.strftime("%d-%m-%Y %H:%M")
    assert isinstance(actualtime, str), f"La valeur retournée n'est pas de type str: {type(actualtime)}"
    return actualtime

def update_website(airportname_complete, actualtime, wind_speed, wind_direction, temperature, humidity, pressure, visibility, clouds,  forecast1, temp_max1, temp_min1, wind_speed1, wind_direction1, precipitation1, pressure1, forecast2, temp_max2, temp_min2, wind_speed2, wind_direction2, precipitation2, pressure2, forecast3, temp_max3, temp_min3, wind_speed3, wind_direction3, precipitation3, pressure3, output_dir):
    """ 
    Cette fonction permet de mettre à jour le site web à l'aide des données entrées

    :param param1: Informations à intégrer dans la page web
    :type param1: list
    :returns: Aucun
    :raises: TypeError   
    """
    #Ouvre le fichier HTML
    f = open(f"{output_dir}/index.html",'w',encoding='utf-8')
    #Met ensuite à jour ce fichier avec les données trouvées
    HTML_INDEX = f""" <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Météo Aéroport</title>
            <link rel="stylesheet" href="CSS/style.css" type="text/css" />
        </head>
        <body>
            <header>
                <h1>Météo Aéroport</h1>
                <h2>{airportname_complete}</h2>
                <h3>{actualtime}</h3>
            </header>
            <article>
            <div class="container">
                <h2>Maintenant</h2>
                <p>Vent : {wind_speed} km/h</p>
                <p>Orientation du vent : {wind_direction}</p>
                <p>Humidité : {humidity}%</p>
                <p>Température : {temperature}°C</p>
                <p>Pression : {pressure} hPa</p>
                <p>Visibilité {visibility}</p>
                <p>Nuages : {clouds}</p>
                <p>Source des données : <a href="https://allmetsat.com">Allmetsat</a></p>
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
                <p>Source des données : <a href="https://meteoblue.com">Meteoblue</a></p>
    
            <div class="container">
                <h2>J+2</h2>
                <p>Prévision : {forecast2}</p>
                <p>Vent : {wind_speed2}</p>
                <p>Orientation du vent : {wind_direction2}</p>
                <p>Température maximale : {temp_max2}</p>
                <p>Température minimale : {temp_min2}</p>
                <p>Précipitations : {precipitation2}</p>
                <p>Pression : {pressure2}</p>
                <p>Source des données : <a href="https://meteoblue.com">Meteoblue</a></p>
                
            <div class="container">
                <h2>J+3</h2>
                <p>Prévision : {forecast3}</p>
                <p>Vent : {wind_speed3}</p>
                <p>Orientation du vent : {wind_direction3}</p>
                <p>Température maximale : {temp_max3}</p>
                <p>Température minimale : {temp_min3}</p>
                <p>Précipitations : {precipitation3}</p>
                <p>Pression : {pressure3}</p>
                <p>Source des données : <a href="https://meteoblue.com">Meteoblue</a></p>
            </div>
            </div>
        </article>
        </body>
    </html>
        """
    f.write(HTML_INDEX)





