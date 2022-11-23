from collections import Counter
import json
import urllib.request
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
data = json.loads(raw_data)

cities = []

# lisää kaikki kaupungit cities listaan
for entry in data:
    city = entry["city"]
    cities.append(city)

# laskee city_count listaan kaikki samat merkkijonot ja
# järjestelee ne yleisin ensin
city_count = Counter(cities).most_common()

# tulostaa city_count listalta ensimmäisen elementin
print(f"Suomen liukkain kaupunki: {city_count[0][0]}")
print()

print("Viisi viimeisintä liukastumisvaroitusta:")
print()

# asettaa city ja date muuttujiin arvot data listan viidestä viimeisestä
# elementistä
for i in range(5):
    city = data[-i - 1]["city"]
    date = data[-i - 1]["updated_at"]
    print(f"{i + 1}: {city}, {date}")
