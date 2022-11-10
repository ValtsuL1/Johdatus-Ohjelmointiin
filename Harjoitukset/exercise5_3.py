import math

running = True

while running:
    radius = int(input("Anna säde:\n"))
    area = math.pi * math.pow(radius, 2)
    area = round(area, 2)
    print(f"Ympyrän pinta-ala: {area}")

    answer = input("Haluatko jatkaa? (k/e)\n")
    if answer == "e":
        running = False
