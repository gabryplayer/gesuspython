
import os
import requests

def ping_website():
    url = input("Inserisci l'URL del sito: ")
    response = os.system("ping -c 4 " + url)

def get_website_info():
    url = input("Inserisci l'URL del sito: ")
    response = requests.get(url)
    print("Codice di stato HTTP:", response.status_code)
    print("Header:")
    for key, value in response.headers.items():
        print(key + ": " + value)

choice = input("[1] IP ATTACK WEBSITE   [2] INFORMATION ATTACK WEBSITE: ")

if choice == "1":
    ping_website()
elif choice == "2":
    get_website_info()
else:
    print("Opzione non valida. Riprova.")