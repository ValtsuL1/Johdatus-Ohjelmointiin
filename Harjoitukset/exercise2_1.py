import math
# suorakulmaisen särmiön sivujen pituudet
rectangle_a = input("Anna särmiön ensimmäisen sivun pituus: ")
rectangle_b = input("Anna särmiön toisen sivun pituus: ")
rectangle_c = input("Anna särmiön kolmannen sivun pituus: ")
rectangle_a = float(rectangle_a)
rectangle_b = float(rectangle_b)
rectangle_c = float(rectangle_c)

rectangle_volume = rectangle_a * rectangle_b * rectangle_c
print(f"Särmiön tilavuus: {rectangle_volume} m3")

# pallon tilavuus
ball_radius = input("Anna pallon säde: ")
ball_radius = float(ball_radius)
ball_volume = 4 / 3 * math.pi * math.pow(ball_radius, 3)
ball_volume = round(ball_volume, 2)
print(f"Pallon tilavuus: {ball_volume} m3")
