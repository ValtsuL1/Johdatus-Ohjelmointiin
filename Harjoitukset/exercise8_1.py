from colorama import Fore
from datetime import datetime

ages = []

# kysyy käyttäjältä syntymävuoden joka henkilölle, ja vähentää tämänhetkisestä vuodesta
# lisää lopuksi ages listaan
for i in range(5):
    age = int(input(f"Anna henkilön {i + 1} syntymävuosi:\n"))
    age = datetime.today().year - age
    ages.append(age)

# tarkistaa onko ikä 0:n ja 125:n välillä, jos on tulostaa vihreänä
# jos ei punaisena
for i in range(5):
    if 0 < ages[i] <= 125:
        print(Fore.GREEN + f"{ages[i]} vuotta, Ikä ok!")
    else:
        print(Fore.RED + f"{ages[i]} vuotta, Ikä ei ole oikeassa muodossa.")
