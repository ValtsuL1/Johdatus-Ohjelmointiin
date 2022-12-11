from functions import city_company_sort

cities = [
    {
        "city": "Rovaniemi",
        "company": "Sampokeskus",
    },
    {
        "city": "Oulu",
        "company": "Myllyoja",
    },
    {
        "city": "Rovaniemi",
        "company": "Rinteenkulma",
    },
    {
        "city": "Rovaniemi",
        "company": "Revontulikeskus",
    },
    {
        "city": "Oulu",
        "company": "Valkea",
    },
    {
        "city": "Oulu",
        "company": "Ideapark",
    },
]

# cities sorted muuttujaan tulee city_company_sort
# funktion palauttama lista, parametrinä cities lista
cities_sorted = city_company_sort(cities)

# tulostaa järjestetyn listan
for city in cities_sorted:
    name = city["city"]
    company = city["company"]
    print(f"{name}: {company}")
