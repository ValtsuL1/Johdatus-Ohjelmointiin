import math
import random
import requests
import os
import operator


def show_personal_info():
    print("Kalle Luja")
    print("Lieksa")
    print("Rekkakuski")


def count_seconds(hours, minutes, seconds):
    # lasketaan total_seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    # palautetaan total_seconds arvo seconds_total muuttujaan
    return total_seconds


def magazine_serial_check(serial):
    # jos alla olevat täyttyy, tulostaa
    # ja palauttaa passed muuttujaan True
    if len(serial) == 9:
        if serial[4] == "-":
            serial_num = serial.replace("-", "")
            if serial_num.isnumeric():
                return True


def show_numbered_list(title, data):
    # tulostaa title:n
    print(title)
    amount = len(data)
    # tulostaa jokaisen listan elementin
    for i in range(amount):
        print(f"{i + 1}. {data[i]}")
    print()


def box_volume(width, height, depth):
    result = round(width * height * depth, 2)
    return result


def ball_volume(radius):
    result = round((4 * math.pi * math.pow(radius, 3)) / 3, 2)
    return result


def pipe_volume(radius, length):
    result = round(math.pi * math.pow(radius, 2) * length, 2)
    return result


def get_lotto_numbers():
    lotto_numbers = []
    # jatkaa kunnes lotto_numbers listassa on 7 elementtiä
    while len(lotto_numbers) < 7:
        # arpoo 1-40 väliltä numeron ja muuttaa sen merkiksi
        number = str(random.randint(1, 40))
        # jos numeroa ei löydy lotto_numbers listasta lisää sen sinne
        if number not in lotto_numbers:
            lotto_numbers.append(number)
    # kun lotto_numbers pituus on 7 yhdistää
    # elementit merkkijonoon ja palauttaa
    lotto_numbers = " ".join(lotto_numbers)
    return lotto_numbers


# get_lotto_bonus_numbers on sama kuin get_lotto_numbers paitsi listassa
# pitää olla 3 elementtiä ja number muuttujan lisäksi lotto_numbers listassa
# ei saa olla main_numbers listan elementtejä, main_numbers parametrinä on
# lotto_numbers lista
def get_lotto_bonus_numbers(main_numbers):
    lotto_numbers = []
    while len(lotto_numbers) < 3:
        number = str(random.randint(1, 40))
        if number not in lotto_numbers and number not in main_numbers:
            lotto_numbers.append(number)
    lotto_numbers = " ".join(lotto_numbers)
    return lotto_numbers


def convert_currency(amount, convert_from, convert_to):
    currencies = ["EUR", "USD", "GBP", "SEK"]

    # asettaa url muuttujaksi web osoitteen johon tulee currencies listasta
    # muunnettava valuutta ja mihin muunnetaan sekä amount
    url = f"https://api.apilayer.com/currency_data/convert?to={currencies[convert_to]}&from={currencies[convert_from]}&amount={amount}"

    # headers muuttujaan tulee dictionary jossa on apikey
    data = {}
    headers = {
        "apikey": "NJxon2Z11rSYgxx7Tj68XeeCxbdpKiIF"
    }

    # requests funktio hakee response muuttujaan tiedot
    response = requests.request("GET", url, headers=headers, data=data)

    # response muutetaan merkkijonosta dictionaryksi json funktiolla
    result = response.json()

    return result


def print_directories():
    for subdir1 in os.listdir("C:\\Program Files\\"):
        try:
            print(f"{subdir1} ...")

            if os.path.isdir(f"C:\\Program Files\\{subdir1}\\"):
                for subdir2 in os.listdir(f"C:\\Program Files\\{subdir1}\\"):
                    print(f"- {subdir2}")

                    if os.path.isdir(f"C:\\Program Files\\{subdir1}\\{subdir2}\\"):
                        for subdir3 in os.listdir(f"C:\\Program Files\\{subdir1}\\{subdir2}\\"):
                            print(f"-- {subdir3}")

        except PermissionError:
            print("Käyttö estetty")
            continue


def print_folders(main_dir):
    if os.path.isdir(main_dir):
        for subdir in os.listdir(main_dir):
            try:
                print(subdir)

                subdir1 = f"{main_dir}{subdir}\\"
                print_folders(subdir1)

                subdir2 = f"{main_dir}{subdir}{subdir1}\\"
                print_folders(subdir2)

            except PermissionError:
                print("Käyttö estetty")
                continue


def city_company_sort(data):
    # järjestää data listan sorted funktiolla, järjestää ensin city
    # elementin perusteella sitten company
    data_sorted = sorted(data, key=lambda k: (k["city"], k["company"]))
    return data_sorted
