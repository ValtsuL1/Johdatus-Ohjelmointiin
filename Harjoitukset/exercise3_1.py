firstnumber = input("Anna ensimmäinen luku: ")
secondnumber = input("Anna toinen luku: ")
firstnumber = int(firstnumber)
secondnumber = int(secondnumber)

if firstnumber > secondnumber:
    print(f"Suurempi luku: {firstnumber}")
if secondnumber > firstnumber:
    print(f"Suurempi luku: {secondnumber}")
if firstnumber == secondnumber:
    print("Numerot ovat yhtä suuria.")
