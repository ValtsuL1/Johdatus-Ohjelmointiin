# HUOM: tällä rajapinnalla mitä käytin on rajallinen määrä kutsuja
# tällä hetkellä noin 90
from functions import convert_currency

currencies = ["EUR", "USD", "GBP", "SEK"]

amount = float(input("Syötä rahasumma:\n"))
print()

print("EUR: 1, USD: 2, GBP: 3, SEK: 4")
convert_from = int(input("Syötä muunnettava valuutta:\n")) - 1
convert_to = int(input("Mihin valuuttaan muunnetaan?\n")) - 1

# result muuttujaan saadaan convert_currency funktiolla dictionary
# parametrit ovat käyttäjän antamia
result = convert_currency(amount, convert_from, convert_to)
# converted_amount muuttuja on result dictionarystä "result" elementti
# pyöristettynä kahdella
converted_amount = round(result["result"], 2)

print(f"{amount} {currencies[convert_from]}: {converted_amount} {currencies[convert_to]}")
