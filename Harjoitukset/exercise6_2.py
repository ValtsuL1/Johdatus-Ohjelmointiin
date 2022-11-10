
while True:

    # kysyy numeron käyttäjältä
    number = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))

    # jos numero on 1-10, tulostaa kertotaulun annetulle numerolle
    if 1 <= number <= 10:
        for x in range(1, 11):
            newNumber = number * x
            print(f"{number} x {x} = {newNumber}")

    # jos numero on vähemmän kuin yksi lopettaa ohjelman
    elif number == 0:
        break

    # jos numero on enemmän kuin 10 tai negatiivinen,
    # ilmoittaa väärästä luvusta ja jatkaa ohjelmaa
    else:
        print("Vääränlainen luku.")
