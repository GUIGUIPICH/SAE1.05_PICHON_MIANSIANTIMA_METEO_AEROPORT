import requests
from bs4 import BeautifulSoup

url = "https://fr.allmetsat.com/metar-taf/france.php?icao=LFBI"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    wind_direction = soup.find(text="Vent").find_next('b').text
    wind_speed = soup.find(text="Vent").find_next('b').find_next('b').text
    temperature = soup.find(text="Température").find_next('b').text
    humidity = soup.find(text="Humidité").find_next('b').text
    pressure = soup.find(text="Pression").find_next('b').text
    clouds = soup.find(text="Nuages").find_next('b').text
    visibility = soup.find(text="Visibilité").find_next('b').text

    print(f"Direction du vent : {wind_direction}")
    print(f"Vitesse du vent : {wind_speed}")
    print(f"Température : {temperature}°C")
    print(f"Taux d'humidité : {humidity}%")
    print(f"Pression atmosphérique : {pressure} hPa")
    print(f"Densité des nuages : {clouds}")
    print(f"Visibilité : {visibility}")
else:
    print(f"Échec de la requête avec le code de statut : {response.status_code}")



# wind_direction = soup.find("div", class_="mt").text.split()[1]
# wind_speed = soup.find("div", class_="mt").text.split()[2]
# temperature = soup.find("div", class_="mt").text.split()[4][:-1]  # Enlever le symbole °C
# humidity = soup.find("div", class_="mt").text.split()[6][:-1]  # Enlever le symbole %
# pressure = soup.find("div", class_="mt").text.split()[8]
# cloud_density = soup.find("div", class_="mt").text.split()[12]
# visibility = soup.find("div", class_="mt").text.split()[-3]
