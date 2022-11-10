import random

random_number = random.randint(2, 10)
print(f"Arvottu luku: {random_number}")

rectangle_side1 = random.randint(2, 10)
rectangle_side2 = random.randint(2, 10)
rectangle_area = rectangle_side1 * rectangle_side2

print(f"Arvottu 1. sivu: {rectangle_side1}")
print(f"Arvottu 2. sivu: {rectangle_side2}")
print(f"Arvotuista sivuista laskettu pinta-ala: {rectangle_area}")
