cities = ["Rooma", "Ateena", "Tukholma", "Lontoo", "Dublin", "Pariisi"]

# laittaa listan aakkosjärjestykseen
cities_sorted = sorted(cities)

# laskee listassa olevien kaupunkien lukumäärän
amount = len(cities_sorted)

# asettaa city muuttujalle arvon cities_sorted listasta
# index muuttujan perusteella
# lopuksi tulostaa indexin (+1) ja kaupungin
for index in range(amount):
    city = cities_sorted[index]
    print(f"{index + 1}: {city}")