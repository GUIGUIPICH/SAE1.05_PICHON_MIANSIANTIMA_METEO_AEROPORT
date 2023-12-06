import requests
from bs4 import BeautifulSoup
import re


url = "https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = response.text

    # wind_direction = soup.find("div", class_="mt").text.split()[1]
    # wind_speed = soup.find("div", class_="mt").text.split()[2]
    # temperature = soup.find("div", class_="mt").text.split()[4][:-1]
    # humidity = soup.find("div", class_="mt").text.split()[6][:-1] 
    # pressure = soup.find("div", class_="mt").text.split()[8]
    # cloud_density = soup.find("div", class_="mt").text.split()[12]
    # visibility = soup.find("div", class_="mt").text.split()[-3]
    
    wind_direction = re.search(r"Vent\s*(\d+)\s*kt", content)
    wind_speed = re.search(r"Vent\s*\d+\s*kt\s*de\s*[^<]*<b>([^<]+)</b>", content)
    temperature = re.search(r"Température\s*<b>([^<]+)</b>", content)
    humidity = re.search(r"Humidité\s*<b>([^<]+)</b>", content)
    pressure = re.search(r"Pression\s*<b>([^<]+)</b>", content)
    clouds = re.search(r"Nuages\s*<b>([^<]+)</b>", content)
    visibility = re.search(r"Visibilité\s*([^<]+)</div>", content)
    
    print(f"Direction du vent : {wind_direction}")
    print(f"Vitesse du vent : {wind_speed}")
    print(f"Température : {temperature}°C")
    print(f"Taux d'humidité : {humidity}%")
    print(f"Pression atmosphérique : {pressure} hPa")
    print(f"Densité des nuages : {clouds}")
    print(f"Visibilité : {visibility}")
else:
    print(f"Échec de la requête avec le code de statut : {response.status_code}")




