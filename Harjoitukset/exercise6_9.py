running = True

while running:
    original_price = int(input("Alkuperäinen hinta:\n"))
    manufacture_year = int(input("Valmistusvuosi:\n"))
    mileage = int(input("Ajokilometrit:\n"))
    category = int(input("Hintakategoria (1/2):\n"))
    importq = input("Onko tuontiauto? (k/e)\n")

    total_years = 2022 - manufacture_year

    is_import = False
    if importq == "k":
        is_import = True

    average_mileage = mileage / total_years

    # alla on laskukaavan mukaisesti molemmille kategorioille laskettu auton
    # lopullinen hinta
    if category == 1:
        if average_mileage >= 30000:
            if total_years >= 5:
                new_price = original_price * 0.65 * (0.04 * total_years - 5)
            else:
                new_price = original_price * (0.07 * total_years)
        else:
            if total_years >= 5:
                new_price = original_price * 0.75 * (0.03 * total_years - 5)
            else:
                new_price = original_price * (0.05 * total_years)
        if new_price < original_price * 0.18:
            new_price = original_price * 0.18
        else:
            pass
    else:
        if average_mileage >= 30000:
            if total_years >= 5:
                new_price = original_price * 0.5 * (0.07 * total_years - 5)
            else:
                new_price = original_price * (0.1 * total_years)
        else:
            if total_years >= 5:
                new_price = original_price * 0.6 * (0.05 * total_years - 5)
            else:
                new_price = original_price * (0.08 * total_years)
        if new_price < original_price * 0.12:
            new_price = original_price * 0.12
        else:
            pass
    if is_import:
        new_price = new_price * 1.24
    else:
        pass

    new_price = round(new_price, 2)

    print(f"Auton myyntihinta: {new_price} €")
    continueq = input("Haluatko syöttää uudet tiedot? (k/e)\n")
    if continueq == "e":
        print("Kiitos ohjelman käytöstä!")
        running = False
    else:
        continue
