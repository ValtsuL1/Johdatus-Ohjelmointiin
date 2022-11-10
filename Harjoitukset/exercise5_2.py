totalRain = 0

for x in range(12):
    rainAmount = int(input("Anna kuukauden sademäärä:\n"))
    totalRain = totalRain + rainAmount

averageRain = totalRain / 12

print(f"Vuoden keskiarvo on n. {averageRain} mm")
