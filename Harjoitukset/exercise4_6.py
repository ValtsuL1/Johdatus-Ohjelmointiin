temperature = int(input("Anna ulkolämpötila:\n"))
moisture = int(input("Anna kosteusprosentti:\n"))

freezing = False
heatwave = False
raining = False
hailstorm = False

# määrittelee onko pakkasta vai hellettä
if temperature < 0:
    freezing = True
elif temperature > 20:
    heatwave = True

# määrittelee sataako vettä vai rakeita
if moisture > 80:
    if temperature < -20:
        hailstorm = True
    else:
        raining = True

# tulostaa muuttuujien perusteella sään
print(f"Lämpötila: {temperature} °C")

if freezing:
    print("Pakkasta.")

if raining:
    if heatwave:
        print("Kosteaa ja tukalaa.")
    else:
        print("Sataa.")

if hailstorm:
    print("Sataa rakeita!")

if heatwave and not raining:
    print("Helleaalto!")
