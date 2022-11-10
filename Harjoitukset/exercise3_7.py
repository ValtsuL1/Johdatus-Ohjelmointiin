import math

postageType = input("Anna lähetyksen tyyppi. (kirje/paketti): ")
isLetter = None

if postageType == "kirje":
    isLetter = True
if postageType == "paketti":
    isLetter = False

postageWeight = input("Anna lähetyksen paino grammoina: ")
postageWeight = float(postageWeight)

# kirjeen lähetyskulujen määritys
if isLetter == True:
    if postageWeight < 200:
        addCost = 0
    if 200 <= postageWeight <= 500:
        postageWeight = postageWeight / 100
        postageWeight = math.trunc(postageWeight)
        addCost = postageWeight * 100 * 0.04 / 100
    if postageWeight > 500:
        postageWeight = postageWeight / 100
        postageWeight = math.trunc(postageWeight)
        addCost = postageWeight * 100 * 0.07 / 100
        canFit = input("Mahtuuko kirje postilaatikkoon? (k/e): ")
        if canFit == "e":
            addCost = addCost + 2
    postageCost = addCost + 0.50
    print(f"Lähetyksen hinta: {postageCost} €")

# paketin lähetyskulujen määritys
if isLetter == False:
    if postageWeight < 200:
        addCost = 0
    if 200 <= postageWeight <= 500:
        postageWeight = postageWeight / 100
        postageWeight = math.trunc(postageWeight)
        addCost = postageWeight * 100 * 0.08 / 100
    if postageWeight > 500:
        postageWeight = postageWeight / 100
        postageWeight = math.trunc(postageWeight)
        addCost = postageWeight * 100 * 0.14 / 100
    postageCost = addCost + 2
    print(f"Lähetyksen hinta: {postageCost} €")
