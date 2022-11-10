import math

a = input("Anna a:n arvo: ")
a = float(a)
b = input("Anna b:n arvo: ")
b = float(b)
c = input("Anna c:n arvo: ")
c = float(c)

x1 = ((-b) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)

x2 = ((-b) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)

print(x1)
print(x2)
