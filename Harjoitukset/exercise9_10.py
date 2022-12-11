import random

# asettaa odd_num muuttujaan lambda joka palauttaa
# True jos annettu luku on pariton
odd_num = lambda a: a % 2 != 0

# lista johon kerätään satunnaiset numerot
number_list = []

# lisää number_list 10 satunnaista numeroa 1-10 väliltä
for i in range(10):
    number = random.randint(1, 10)
    number_list.append(number)

# lisää odd_numbers listaan number_list
# listan parittomat luvut
odd_numbers = list(filter(odd_num, number_list))

# lisää number_values listaan booleanin sen mukaan
# onko number_list listan numero pariton vai parillinen
number_values = list(map(odd_num, number_list))

# tulostaa listat
print(odd_numbers)
print(number_values)
