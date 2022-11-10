number = 1
number2 = 1
sumTotal = 0
years = ""

# kun numero on vähemmän kuin 50, tulostaa ja lisää yhden
while number <= 50:
    print(number)
    number = number + 1

# tulostaa numeron ja lisää yhden 50 kertaa
for x in range(50):
    print(number2)
    number2 = number2 + 1

# lisää sumTotal muuttujaan jokaisen arvon 1-30 väliltä
for x in range(31):
    sumTotal = sumTotal + x

# lisää years muuttujaan vuodet 2005-2010 ja väliviivat jokaisen jälkeen
for x in range(2005, 2011):
    years = years + str(x) + " "

# poistaa viimeisen väliviivan years muuttujasta
years = years[0:-1]

print(f"Summa: {sumTotal}")
print(years)
