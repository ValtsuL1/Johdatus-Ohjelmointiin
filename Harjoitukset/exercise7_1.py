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

services = []
locations = cafe["location"]

print(cafe["name"])
print(locations["address"])
print(locations["zip_code"], locations["city"])
print()
print(cafe["website"])

for service in cafe["categories"]:
    services.append(service)

print(f"Palvelut: {services}")