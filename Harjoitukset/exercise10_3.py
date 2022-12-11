import random

# luo listan johon saadaan sisältö wisewords.txt tiedostosta
wisewords_list = []

file_handle = open("wisewords.txt", "r", encoding="utf-8")

# lisää wisewords_list joka rivin wisewords.txt tiedostosta
while True:
    line = file_handle.readline()
    wisewords_list.append(line)

    if not line:
        break
file_handle.close()

# määrittelee muuttujaan random_indexille ylärajan
max_index = len(wisewords_list) - 1

# random_index on järjestysluku wisewords_list listalle
random_index = random.randint(1, max_index)

# tulostaa wisewords_list listasta satunnaisen itemin
print(f"Päivän mietelause:\n{wisewords_list[random_index]}")
