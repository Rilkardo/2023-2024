import requests
import json 

URL = "https://itunes.apple.com/search?entity=song&limit=20&term=weezer"

atbilde = requests.get(URL)

print(atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))
#konkrēta lieluma izvadīšana 
#print(dati["results"][0]["trackName"])
#print(dati["results"][1]["trackName"])

#Izveido veidu, kā var iegūt jebkādu skaitu ar dziesmu nosaukumu. piemēram, ja pieprasijums tiks prasitas 20 dziesmas

for a in dati["results"]:
    nosaukums = a["trackName"]
    print (nosaukums)