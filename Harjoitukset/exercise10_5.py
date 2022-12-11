import json
from datetime import datetime
import os

# tarkistaa onko maintenance.json olemassa ja luo sen jos ei ole
if not os.path.isfile("maintenance.json"):
    file_handle = open("maintenance.json", "x")
    content = []
    json_data = json.dumps(content)
    file_handle.write(json_data)
    file_handle.close()
else:
    pass

# asettaa entries muuttujaan maintenance.json sisällön
file_handle = open("maintenance.json", "r")
content = file_handle.read()
file_handle.close()
entries = json.loads(content)

# entries_length määritellään onko lista tyhjä
# sekä viimeisimmän dictionaryn indeksi
entries_length = len(entries)

# jos entries listassa on vähintään yksi dictionary
# tulostaa dictionaryn jonka indeksi on aina listan viimeinen
if entries_length > 0:
    date = entries[entries_length - 1]["date"]
    name = entries[entries_length - 1]["name"]
    code = entries[entries_length - 1]["code"]
    desc = entries[entries_length - 1]["desc"]
    print("Viimeisin kirjaus...")
    print(f"Pvm: {date}")
    print(f"Hlö: {name}")
    print(f"Tilannekoodi: {code}")
    print(f"Viesti: {desc}")
    print()
else:
    pass

# kysyy käyttäjältä uuden kirjauksen
print("Uusi kirjaus...")
name = input("Kirjaajan nimi:\n")
code = input("Tilannekoodi:\n")
desc = input("Selite:\n")

date = datetime.now()
date = date.strftime("%d/%m/%Y")

# tallentaa entry dictionaryyn joka lisätään entries listaan
entry = {
            "date": date,
            "name": name,
            "code": code,
            "desc": desc
        }

entries.append(entry)

# kirjoittaa maintenance.json päälle uuden entries listan
file_handle = open("maintenance.json", "w")
json_data = json.dumps(entries)
file_handle.write(json_data)
file_handle.close()
