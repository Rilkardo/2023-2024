#laika noteikšana 

import requests 

URL = "http://worldtimeapi.org/api/timezone/Europe/Riga"

dati = requests.get(URL)

print(dati)

laiksLatvija = dati.json()

print(laiksLatvija)

print(laiksLatvija["uts_datetime"])

#asv laiks,ņujorka
url2 = "https://worldtimeapi.org/timezone/America/New_York"
dati2 = requests.get(url2)
print(dati2)
laiksnewyork = dati2. json()
print(laiksnewyork)["datetime"]
