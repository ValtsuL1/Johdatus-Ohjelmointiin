road_travel = input("Matka-ajon kilometrit: ")
city_travel = input("Kaupunki-ajon kilometrit: ")
road_travel = float(road_travel)
city_travel = float(city_travel)
road_travel = road_travel * (5.1 / 100)
city_travel = city_travel * (7.5 / 100)
fuel_consumption = road_travel + city_travel
fuel_consumption = round(fuel_consumption, 2)
print(f"Kulutus: {fuel_consumption} l")
