number = 0

try:
    for x in range(5):
        newNumber = int(input("Anna numero:\n"))

        # varmistaa että luku on positiivinen, lopettaa jos ei ole
        if newNumber < 0:
            print("Anna vain positiivisia lukuja!")
            break

        # korvaa number muuttujan jos newNumber on isompi kuin aikaisempi
        if newNumber > number:
            number = newNumber

# varmistaa että käyttäjä antaa vain kokonaislukuja
except ValueError:
    print("Anna vain kokonaislukuja!")

print(f"Suurin käyttäjän luku: {number}")
