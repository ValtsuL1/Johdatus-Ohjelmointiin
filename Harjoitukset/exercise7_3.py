shopcart = [
 {"name": "Lokki-valaisin", "price": 349.9},
 {"name": "Stockholm-matto", "price": 129.9},
 {"name": "Malm-lipasto", "price": 49.9},
 {"name": "Vienna-divaanisohva", "price": 799.9},
 {"name": "Ritz-nojatuoli", "price": 369.9}
]

price = 0

print("Kuitti ostoksista:")

for item in shopcart:
    name = item["name"]
    print(f"- {name}")
    # lisää price muuttujaan jokaisen esineen hinnan
    price = price + item["price"]

vat = price - (price / 1.24)
vat = round(vat, 2)

print()
print(f"Yhteensä {price} €, arvonlisävero {vat} €.")
print("Tervetuloa uudelleen!")