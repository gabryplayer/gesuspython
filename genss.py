import random
import string
def genera_codici_playstation(num_codici):
    codici = []
    for _ in range(num_codici):
        codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        codici.append(codice)
    return codici

def genera_codici_amazon(num_codici):
    codici = []
    for _ in range(num_codici):
        codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        codici.append(codice)
    return codici

def genera_codici_fortnite(num_codici):
    codici = []
    for _ in range(num_codici):
        codice = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        codici.append(codice)
    return codici

def genera_codici_roblox(num_codici):
    codici = []
    for _ in range(num_codici):
        codice = 'RI-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        codici.append(codice)
    return codici

def crea_file_codici(codici, nome_file):
    with open(nome_file, "w") as file:
        for codice in codici:
            file.write(codice + '\n')

opzioni = ["1 - Genera codici PlayStation",
           "2 - Genera codici Amazon",
           "3 - Genera codici Fortnite",
           "4 - Genera codici Roblox"]

print("GENERATOR BY dakis-yu 45 vouches#0425")
print("Seleziona il tipo di codice da generare:")
for opzione in opzioni:
    print(opzione)

scelta = int(input("Inserisci il numero corrispondente all'opzione scelta: "))
num_codici = int(input("Inserisci il numero di codici da generare: "))

if scelta == 1:
    codici = genera_codici_playstation(num_codici)
    nome_file = "playstation_16_codes.txt"
elif scelta == 2:
    codici = genera_codici_amazon(num_codici)
    nome_file = "amazon_16_codes.txt"
elif scelta == 3:
    codici = genera_codici_fortnite(num_codici)
    nome_file = "fortnite_codes.txt"
elif scelta == 4:
    codici = genera_codici_roblox(num_codici)
    nome_file = "roblox_codes.txt"
else:
    print("Opzione non valida.")

crea_file_codici(codici, nome_file)
print(f"Il file {nome_file} è stato creato con successo con {num_codici} codici.")
