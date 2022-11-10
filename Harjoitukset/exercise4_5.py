student_q = input("Oletko opiskelija? (k/e)\n")

discount = False
student = False

if student_q == "k":
    student = True

month = int(input("Mille kuukaudelle matka varataan? (1/12)\n"))

# jos kuukausi on 6-8, discount muuttuja pysyy falsena
if not 5 < month < 9:
    if student:
        discount = True

if discount:
    print("Alennus myönnetty!")
else:
    print("Normaali hinta.")
