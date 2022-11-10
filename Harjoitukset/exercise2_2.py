import math
triangle_a = input("Anna kolmion ensimmäinen kateetti: ")
triangle_b = input("Anna kolmion toinen kateetti: ")
triangle_a = float(triangle_a)
triangle_b = float(triangle_b)
triangle_hypotenuse = math.sqrt(math.pow(triangle_a, 2) + math.pow(triangle_b, 2))
triangle_hypotenuse = round(triangle_hypotenuse, 2)
print(f"Hypotenuusan pituus: {triangle_hypotenuse} m")
