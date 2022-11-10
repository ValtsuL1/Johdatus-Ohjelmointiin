from datetime import datetime

name = "Aku Ankka"
birthdate = "2000"
balance = "1500"
date = datetime.now()
date = date.strftime("%d.%m.%Y")

print(f"{name} ({birthdate}), saldo: {balance} €, päivitetty {date}.")
