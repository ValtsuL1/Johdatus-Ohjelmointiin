from functions import magazine_serial_check

serial = input("Anna ISSN-sarjanumero:\n")

# passed muuttujan arvo saadaan
# magazine_serial_check funktiolla
# jonka parametri on käyttäjän antama merkkijono
passed = magazine_serial_check(serial)

if passed:
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")
