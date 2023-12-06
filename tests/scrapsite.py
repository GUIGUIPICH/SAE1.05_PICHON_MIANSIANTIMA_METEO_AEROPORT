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
    
    c1b_div = soup.find('div', class_='c1b')
    c1b_content = str(c1b_div)
    
    wind_speed = re.search(r"Vent\s*<b>([^<]+)</b>", c1b_content)
    wind_direction = re.search(r"Vent\s*<b>\d+</b>\s*kt de <b>([^<]+)</b>", c1b_content)
    temperature = re.search(r"Température\s*<b>([^<]+)</b>", c1b_content)
    humidity = re.search(r"Humidité\s*<b>([^<]+)</b>", c1b_content)
    pressure = re.search(r"Pression\s*<b>([^<]+)</b>", c1b_content)
    clouds = re.search(r"Nuages\s*<b>([^<]+)</b>", c1b_content)
    visibility = re.search(r"Visibilité\s*([^<]+)</div>", c1b_content)
    
    c1_div = soup.find('div', class_='c1')
    c1_content = str(c1_div)
    
    wind_speed2 = re.search(r"Vent\s*<b>([^<]+)</b>", c1_content)
    wind_direction2 = re.search(r"Vent\s*<b>\d+</b>\s*kt de <b>([^<]+)</b>", c1_content)
    temperature2 = re.search(r"Température\s*<b>([^<]+)</b>", c1_content)
    humidity2 = re.search(r"Humidité\s*<b>([^<]+)</b>", c1_content)
    pressure2 = re.search(r"Pression\s*<b>([^<]+)</b>", c1_content)
    clouds2 = re.search(r"Nuages\s*<b>([^<]+)</b>", c1_content)
    visibility2 = re.search(r"Visibilité\s*([^<]+)</div>", c1_content)
    
    print("Maintenant \n")
    
    if wind_speed:
        print(f"Vitesse du vent : {wind_speed.group(1)} kt")
    else:
        print("Vitesse du vent : Inconnu")
    if wind_direction:
        print(f"Direction du vent : {wind_direction.group(1)}")
    else:
        print("Direction du vent : Inconnu")
    if temperature:
        print(f"Température : {temperature.group(1)} °C")
    else:
        print("Température : Inconnu")
    if humidity:
        print(f"Taux d'humidité : {humidity.group(1)} %")
    else:
        print("Taux d'humidité : Inconnu")
    if pressure:
        print(f"Pression atmosphérique : {pressure.group(1)} hPa")
    else:
        print("Pression atmosphérique : Inconnu")
    if visibility:
        print(f"Visibilité : {visibility.group(1)}")
    else :
        print("Visibilité : Inconnu")
    if clouds:
        print(f"Densité des nuages : {clouds.group(1)}")
    else:
        print("Densité des nuages : Inconnu")
    
    print("\n24 Prochaines heures \n")
    
    if wind_speed2:
        print(f"Vitesse du vent : {wind_speed2.group(1)} kt")
    else:
        print("Vitesse du vent : Inconnu")
    if wind_direction2:
        print(f"Direction du vent : {wind_direction2.group(1)}")
    else:
        print("Direction du vent : Inconnu")
    if temperature2:
        print(f"Température : {temperature2.group(1)} °C")
    else:
        print("Température : Inconnu")
    if humidity2:
        print(f"Taux d'humidité : {humidity2.group(1)} %")
    else:
        print("Taux d'humidité : Inconnu")
    if pressure2:
        print(f"Pression atmosphérique : {pressure2.group(1)} hPa")
    else:
        print("Pression atmosphérique : Inconnu")
    if visibility2:
        print(f"Visibilité : {visibility2.group(1)}")
    else :
        print("Visibilité : Inconnu")
    if clouds2:
        print(f"Densité des nuages : {clouds2.group(1)}")
    else:
        print("Densité des nuages : Inconnu")
else:
    print(f"Échec de la requête avec le code de statut : {response.status_code}")




