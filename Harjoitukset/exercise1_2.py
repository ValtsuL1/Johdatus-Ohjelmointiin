

price = input("Anna hinta ilman alv: ")
price = float(price)
price = price * 1.24
price = round(price, 2)

print(f"Hinta alv:n kanssa: {price} €")