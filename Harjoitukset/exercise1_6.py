totalmoney = input("Anna 1-100 senttiä: ")
totalmoney = int(totalmoney)
cents_50 = totalmoney / 50
cents_50 = int(cents_50)
cents_20 = totalmoney % 50 / 20
cents_20 = int(cents_20)
cents_10 = totalmoney % 50 % 20 / 10
cents_10 = int(cents_10)
cents_5 = totalmoney % 50 % 20 % 10 / 5
cents_5 = int(cents_5)
cents_2 = totalmoney % 50 % 20 % 10 % 5 / 2
cents_2 = int(cents_2)
cents_1 = totalmoney % 50 % 20 % 10 % 5 % 2 / 1
cents_1 = int(cents_1)
print(f"50 snt kolikoita {cents_50} kpl\n20 snt kolikoita {cents_20} kpl\n"
      f"10 snt kolikoita {cents_10} kpl\n5 snt kolikoita {cents_5} kpl\n"
      f"2 snt kolikoita {cents_2} kpl\n1 snt kolikoita {cents_1} kpl")
