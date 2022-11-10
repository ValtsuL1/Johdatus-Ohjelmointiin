money = input("Anna rahaa:\n")
price = input("Ostosten hinta:\n")
money = int(money)
price = int(price)

if money >= price:
    remainder = money - price
    print(f"Kiitos. Annetaan takaisin {remainder} €")

if money < price:
    moreMoney = input("Rahat eivät riitä, anna lisää rahaa:\n")
    moreMoney = int(moreMoney)
    money = money + moreMoney
    if money < price:
        print("Sinulla ei ole tarpeeksi rahaa.")
    if money >= price:
        remainder = money - price
        print(f"Kiitos. Annetaan takaisin {remainder} €")
