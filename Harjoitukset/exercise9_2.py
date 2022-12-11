from functions import count_seconds

time = input("Anna aika muodossa: (h min sek)\n")

# luo times_list listan joka koostuu times merkkijonon merkeistä
# välilyönnillä eroteltuna
time_list = time.split(" ")
# erotetaan jokaisesta time_list listan elementistä pelkkä numero
# poistamalla viimeisiä merkkejä
hours = int(time_list[0][:-1])
minutes = int(time_list[1][:-3])
seconds = int(time_list[2][:-3])

# seconds_total muuttujaksi kutsutaan funktio count_seconds
# parametrillä time joka kysyttiin käyttäjältä
seconds_total = count_seconds(hours, minutes, seconds)

print(f"Yhteensä {seconds_total} sekuntia.")
