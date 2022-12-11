import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# asettaa kuvaukset tolpille
number_labels = ["Numero 1", "Numero 2", "Numero 3", "Numero 4", "Numero 5"]
numbers = []
count = 1

print("Anna viisi numeroa: (0-100)")

# jatkaa kunnes numbers listassa on viisi lukua
while len(numbers) < 5:
    # count muuttujalla saadaan kyseinen numero mikä pitää antaa
    number = int(input(f"Numero {count}:\n"))
    # jos number on 0:n ja 100:n välissä, lisää sen numbers listaan
    # korottaa myös count muuttujan yhdellä
    if 0 <= number <= 100:
        numbers.append(number)
        count = count + 1
    else:
        print("Väärä arvo")

# asettaa värit tolpille
bar_colors = ["tab:red", "tab:blue", "tab:green", "tab:orange", "tab:purple"]

# asettaa parametrit diagrammille number_labels on tolppien kuvaus, numbers
# asettaa tolpille arvot, color on bar_colors listassa olevat värit
ax.bar(number_labels, numbers, color=bar_colors)

# asettaa otsikon ja sivutekstin
ax.set_ylabel("maksimi numero")
ax.set_title("Numerot")

# näyttää diagrammin omassa ikkunassaan
plt.show()
