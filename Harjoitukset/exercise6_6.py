basket = ["omena", "banaani", "kirsikka", "porkkana", "peruna", "tomaatti", "kaali"]

choice = input("Syötä sana:\n")

amount = len(basket)

# jos käyttäjää syöttää luvun muuttaa sen ensin integeriksi (-1)
# ja asettaa basket listasta sille vastaavan sanan choice muuttujaan
if choice.isnumeric():
    choice = int(choice) - 1
    choice = basket[choice]
else:
    pass

# jos choice löytyy basket listasta
# poistaa sen sieltä
if choice in basket:
    basket.remove(choice)
    # lopuksi tulostaa uuden listan
    for x in basket:
        print(x)
else:
    print("Sanaa ei löytynyt.")