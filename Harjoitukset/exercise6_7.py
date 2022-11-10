min_number = int(input("Anna alueen alaraja:\n"))
max_number = int(input("Anna alueen yläraja:\n"))

# amount muuttuja koostuu lukujen yhteismäärästä + 1
amount = max_number - min_number + 1
# luo number_list listan range funktiolla jossa pienin luku
# on min_number ja suurin max_number + 1
number_list = list(range(min_number, max_number + 1))

for index in range(amount):
    # jos luku on jaollinen 5:llä jatkaa, jos ei ilmoittaa
    # käyttäjälle ja jatkaa seuraavaan lukuun
    if number_list[index] % 5 == 0:
        # sama luvulla 7
        if number_list[index] % 7 == 0:
            # jos luku on jaollinen 5:llä ja 7:llä ilmoittaa
            # käyttäjälle ja lopettaa
            print(f"Luku {number_list[index]} on jaollinen 5:llä ja 7:llä.")
            print("Lopetetaan haku.")
            break
        else:
            print(f"{number_list[index]} ei ole jaollinen seitsemällä, hylätään.")
            continue
    else:
        print(f"{number_list[index]} ei ole jaollinen viidellä, hylätään.")
        continue
# jos lukualueelta ei löydy sopivaa lukua ilmoittaa
# käyttäjälle ja lopettaa
else:
    print("Lukualueelta ei löytynyt sopivaa numeroa.")
