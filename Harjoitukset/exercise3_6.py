year = input("Anna vuosiluku: ")
year = int(year)

yearRemainder400 = year % 400
if yearRemainder400 == 0:
    print("Karkausvuosi.")
else:
    yearRemainder100 = yearRemainder400 % 100
    if yearRemainder100 == 0:
        print("Ei ole karkausvuosi.")
    else:
        yearRemainder4 = yearRemainder400 % 4
        if yearRemainder4 == 0:
            print("Karkausvuosi.")
        else:
            print("Ei ole karkausvuosi.")