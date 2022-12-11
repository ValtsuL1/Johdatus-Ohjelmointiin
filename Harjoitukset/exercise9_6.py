from functions import get_lotto_numbers, get_lotto_bonus_numbers

# kutsuu lotto_numbers muuttujaan get_lotto_numbers funktion
# ja lotto_bonus_numbers muuttujaan get_lotto_bonus_numbers
# jonka parametrinä on lotto_numbers lista
lotto_numbers = get_lotto_numbers()
lotto_bonus_numbers = get_lotto_bonus_numbers(lotto_numbers.split(" "))

print(f"Lottorivi: {lotto_numbers}, lisänumerot: {lotto_bonus_numbers}.")