import math

startingCost = input("Anna ostosten kokonaissumma: ")
startingCost = float(startingCost)

isStudent = input("Oletko opiskelija? (k/e): ")
isMember = input("Oletko kanta-asiakas? (k/e): ")

if isMember == "k":
    memberPoints = input("Paljonko sinulla on kanta-asiakaspisteitä?: ")
    memberPoints = float(memberPoints)

discountCodeQ = input("Onko sinulla alennuskoodi? (k/e): ")
if discountCodeQ == "k":
    discountCode = input("Anna alennuskoodi: ")

# kysytään onko alennuskoodia, jos on niin kumpi
if discountCodeQ == "k":
    if discountCode == "FALL22":
        totalCost = startingCost * 0.9
    if discountCode == "BK2SCHOOL" and isStudent == "k":
        totalCost = startingCost * 0.8
if discountCodeQ == "e":
    totalCost = startingCost

# lasketaan mahdolliset kanta-asiakas alennukset hinnasta
if isMember == "k":
    pointsMultiplier = startingCost / 10
    pointsMultiplier = math.trunc(pointsMultiplier)
    memberPoints = ((memberPoints + (pointsMultiplier * 100)) / 1000)
    memberDiscount = math.trunc(memberPoints)
    totalCost = startingCost - (memberDiscount * 5)

# postikulut määritellään hinnasta ennen alennuksia, myös mahdolliset negatiiviset
# luvut muutetaan nolliksi
if startingCost < 99:
    totalCostPost = totalCost + 7.95
    if totalCostPost < 0:
        totalCostPost = 0 + 7.95
if startingCost >= 99:
    totalCost = totalCost
    if totalCost < 0:
        totalCost = 0

if startingCost < 99:
    print(f"Loppusumma: {totalCostPost} €, postikulut: 7,95 €")
if startingCost >= 99:
    print(f"Loppusumma: {totalCost} €, postikulut: 0")
