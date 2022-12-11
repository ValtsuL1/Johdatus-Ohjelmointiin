import json
from datetime import datetime

# tallentaa entries muuttujaan guestbook.json sisällön
file_handle = open("guestbook.json", "r")
content = file_handle.read()
file_handle.close()
entries = json.loads(content)

read_or_write = input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k)\n")

if read_or_write == "k":
    # kysyy uuden viestin käyttäjältä ja tallentaa date muuttujaan päivämäärän ja kellonajan
    text = input("Kirjoita uusi viesti:\n")
    date = datetime.now()
    date = date.strftime("%d/%m/%Y %H:%M:%S")
    # tallentaa entry dictionaryyn text ja date muuttujat
    entry = {
                "text": text,
                "date": date
            }

    # lisää entries listaan entry dictionaryn
    entries.append(entry)
    # tallentaa json_data muuttujaan entries listan
    json_data = json.dumps(entries)

    # avaa guestbook.json ja kirjoittaa päälle uuden entries listan
    file_handle = open("guestbook.json", "w")
    file_handle.write(json_data)
    file_handle.close()
else:
    # tulostaa entries listan entry dictionaryt
    for entry in entries:
        text = entry["text"]
        date = entry["date"]
        print(f"{text} ({date})")
