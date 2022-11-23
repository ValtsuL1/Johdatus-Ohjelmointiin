import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

strongest_wind = 0
weakest_wind = 0
lapland = []
middle = []
south = []

for entry in weather:
    wind = entry["wind"]
    area = entry["area"]
    # jos dictionaryn wind arvo on isompi kuin edellinen,
    # strongest_wind päivittyy uudeksi isoimmaksi,
    # myös strongest_location päivittyy
    if strongest_wind < wind:
        strongest_wind = wind
        strongest_location = entry["location"]
    # sama kuin ylempänä, mutta tässä pitää saada ensimmäinen arvo
    # weakest wind muuttujaan, onnistuu or lauseella
    elif wind < weakest_wind or weakest_wind == 0:
        weakest_wind = wind
        weakest_location = entry["location"]
    # lisää alueiden tuulennopeudet alueen listaan
    if area == "lapland":
        lapland.append(wind)
    elif area == "middle":
        middle.append(wind)
    else:
        south.append(wind)

# laskee alueiden tuulennopeuksien keskiarvot,
# pyöristää samalla yhteen desimaaliin
lapland_average = round(sum(lapland) / len(lapland), 1)
middle_average = round(sum(middle) / len(middle), 1)
south_average = round(sum(south) / len(south), 1)

print(f"Tänään eniten tuulee sijainnissa: {strongest_location}, {strongest_wind} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {weakest_location}, {weakest_wind} m/s")
print()
print(f"Keskimääräinen tuuli, Lappi: {lapland_average} m/s")
print(f"Keskimääräinen tuuli, Maan keskiosa: {middle_average} m/s")
print(f"Keskimääräinen tuuli, Etelä-suomi: {south_average} m/s")
