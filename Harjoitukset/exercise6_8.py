import random
import string


def find_password(pass_length):
    while True:
        # luo characters muuttujan, joka on merkkijono jossa on kaikki
        # isot ja pienet kirjaimet, numerot ja special_characters
        # muuttujassa olevat erikoismerkit
        characters = string.ascii_letters + string.digits + special_characters
        # luo password muuttujan joka koostuu satunnaisista characters
        # muuttujan merkeistä ja joka on käyttäjän antaman length
        # muuttujan pituinen
        password = "".join(random.choice(characters) for i in range(pass_length))
        # katsoo onko vähintään yksi pieni kirjain
        if sum(map(str.islower, password)) >= 1:
            # katsoo onko vähintään yksi iso kirjain
            if sum(map(str.isupper, password)) >= 1:
                # katsoo onko vähintään yksi numero
                if sum(map(str.isnumeric, password)) >= 1:
                    # katsoo onko vähintään yksi merkki special_characters_list listasta
                    if any(x in password for x in special_characters_list):
                        # jos kaikki ehdot täyttyvät, ilmoittaa käyttäjälle salasanan
                        # muuttaa passwordfound muuttujan True:ksi ja poistuu loopista
                        return password
                        # jos yksikään ehdoista ei täyty, hyppää takaisin loopin
                        # alkuun ja generoi uuden satunnaisen password muuttujan
                        # jatkaa kunnes kaikki ehdot täyttyvät


# luo alkuun muuttujan jolla määritellään onko salasana löytynyt
passwordfound = False

# luo special_characters muuttujan johon tulee erikoismerkkejä
# luo siitä myös listan, jota tarvitaan vertailussa
special_characters = "_~?*$#!+%@"
special_characters_list = list(special_characters)

# katsoo alussa onko passwordfound True, jos on lopettaa ohjelman
while True:
    if passwordfound:
        break
    else:
        # kysytään salasanan pituus, jos alle kahdeksan merkkiä
        # ilmoitetaan siitä ja kysytään uudestaan
        length = int(input("Kuinka pitkän salasanan haluat?\n"))
        if length >= 8:
            password = find_password(length)
            print(f"Salasana: {password}")
        else:
            print("Liian lyhyt salasana.")
            continue
