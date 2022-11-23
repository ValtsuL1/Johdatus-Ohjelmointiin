from colorama import Back

for num in range(2, 101):
    # tarkistaa jääkö num muuttujalle yhtäkään jakojäännöstä jakamalla
    # sen jokaisella luvulla 2 ja itsensä välillä
    if all(num % i != 0 for i in range(2, num)):
        # jos ei jää tulostaa numeron vihreällä taustalla
        print(Back.GREEN + str(num))
    else:
        # jos jää, punaisella
        print(Back.RED + str(num))
