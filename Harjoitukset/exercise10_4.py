import json

# tallentaa countries.json sisällön countries muuttujaan
file_handle = open("countries.json", "r")
content = file_handle.read()
countries = json.loads(content)
file_handle.close()

print("Kaikki maat ja pääkaupungit:")

# tulostaa dictionaryt countries listasta
for entry in countries:
    country = entry["country"]
    capital = entry["capital"]
    print(f"{country}: {capital}")

# kysytään käyttäjältä kirjain character muuttujaan
print()
character = input("Minkä alkukirjaimen maat ja pääkaupungit tulostetaan?\n")

# tulostaa dictionaryt jos country muuttujan
# ensimmäinen kirjain on sama kuin character
for entry in countries:
    country = entry["country"]
    capital = entry["capital"]
    if country[0] == character:
        print(f"{country}: {capital}")
