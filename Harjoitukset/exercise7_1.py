cafe = {
 "name": "Imaginary Cafe Oy",
 "website": "https://edu.frostbit.fi/sites/cafe",
 "categories": [
  "cafe",
  "tea",
  "lunch",
  "breakfast"
 ],
 "location": {
  "city": "Rovaniemi",
  "address": "Testikuja 22",
  "zip_code": "96200"
 }
}

# lisää categories listan sisällön services muuttujaan merkkijonona
services = ", ".join(cafe["categories"])
locations = cafe["location"]

print(cafe["name"])
print(locations["address"])
print(locations["zip_code"], locations["city"])
print()
print(cafe["website"])

print(f"Palvelut: {services}")
