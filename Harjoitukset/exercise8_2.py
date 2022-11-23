from colorama import Back, Style
import random

# arpoo number muuttujaan numeron 1 ja 20 väliltä
number = random.randint(1, 20)

while True:
    guess = int(input("Arvaa numero (1-20):\n"))
    # jos guess on pienempi kuin number, sininen tausta
    if guess < number:
        print(Back.BLUE + f"Liian matala")
    # jos isompi, punainen tausta
    elif guess > number:
        print(Back.RED + f"Liian korkea")
    # jos sama, vihreä tausta ja ohjelma päättyy
    else:
        print(Back.GREEN + f"ONNEKSI OLKOON!")
        break
    # jos arvaus ei mennyt oikein resetoidaan taustaväri ennen uutta arvausta
    print(Style.RESET_ALL)