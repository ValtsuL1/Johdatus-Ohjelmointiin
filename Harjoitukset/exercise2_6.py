import math

cherry = (2 + 2 * 2 + 2 - 2 - 2) / 2
apple = ((math.sqrt(3 + 10 - 4)) / 3) + ((math.pow(5, 3) - 5) / 20) + 3
orange = apple - 9
banana = (cherry * 2 - 10) / 3
pear = banana * 3 - 8

result = apple - (banana * 2) + (orange * 2) * (pear + cherry)
result = int(result)
print(f"Vastaus on: {result}")
