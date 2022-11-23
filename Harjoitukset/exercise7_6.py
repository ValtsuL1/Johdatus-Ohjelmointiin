restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 5,
        "location": "Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": [
            "breakfast",
            "lunch"
        ],
        "price_level": 3,
        "location": "Tornio"
    },
    {
        "name": "Snacksy OY",
        "rating": 3.2,
        "reservations": False,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 2,
        "location": "Oulu"
    },
    {
        "name": "Stadin Chili",
        "rating": 4.0,
        "reservations": False,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 2,
        "location": "Kajaani"
    },
    {
        "name": "Pancho Villa",
        "rating": 3.8,
        "reservations": True,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 3,
        "location": "Rovaniemi"
    }
]

# luo listan johon lisätään ehdot täyttävät ravintolat
good_restaurants = []

need_reservation = False

# kysyy käyttäjältä ehdot
print("Tervetuloa ravintolahakuun!")
min_rating = float(input("Monenko tähden ravintolan haluat vähintään? (1-5)\n"))
max_price_level = int(input("Minkä hinta-tason ravintolan haluat maksimissaan? (1-5)\n"))
reservation_q = input("Haluatko tehdä etukäteen varauksen? (k/e)\n")
time = int(input("Mihin kellonaikaan haluat ruokailla? (0 – 23)\n"))

if reservation_q == "k":
    need_reservation = True

# määrittelee käyttäjän antaman time muuttujan perusteella,
# mikä merkkijono pitää löytyä services osiosta
if 6 <= time <= 10:
    dining_time = "breakfast"
elif 11 <= time <= 16:
    dining_time = "lunch"
elif 17 <= time <= 23:
    dining_time = "dinner"
else:
    dining_time = "night"

# luo alkuun muuttujat ravintolan eri elementeille
for restaurant in restaurants:
    name = restaurant["name"]
    rating = restaurant["rating"]
    services = restaurant["services"]
    price_level = restaurant["price_level"]
    location = restaurant["location"]
    reservations = restaurant["reservations"]

    # vertaillaan käyttäjän antamia arvoja ravintolan joka elementtiin,
    # jos jokin ei täyty aloittaa alusta listan seuraavalla ravintolalla
    if min_rating <= rating:
        if max_price_level >= price_level:
            if dining_time in services:
                # jos käyttäjä ei tarvinnut varausta, hyppää seuraavan
                # vertailun yli ja lisää ravintolan
                # name arvon good_restaurants listaan suoraan
                if need_reservation:
                    if reservations:
                        good_restaurants.append(name)
                else:
                    good_restaurants.append(name)

# jos good_restaurants lista ei ole tyhjä sen arvo on True
# ja ehto täyttyy
if good_restaurants:
    print("Sopivat ravintolat:")
    for i in good_restaurants:
        print(i)
else:
    print("Valitettavasti sopivaa ravintolaa ei löytynyt!")
