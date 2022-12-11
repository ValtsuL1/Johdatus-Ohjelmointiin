from functions import box_volume, ball_volume, pipe_volume

while True:
    choice = int(input("Valitse toimenpide (1-3), 0 lopettaa ohjelman:\n"))

    # kysyy käyttäjältä parametrit funktioihin
    # ja tulostaa tuloksen
    if choice == 1:
        box_width = float(input("Anna laatikon leveys:\n"))
        box_height = float(input("Anna laatikon korkeus:\n"))
        box_depth = float(input("Anna laatikon syvyys:\n"))

        result = box_volume(box_width, box_height, box_depth)
        print(f"Laatikon tilavuus: {result} m3")
        print()

    if choice == 2:
        ball_radius = float(input("Anna pallon säde:\n"))

        result = ball_volume(ball_radius)
        print(f"Pallon tilavuus: {result} m3")
        print()

    if choice == 3:
        pipe_radius = float(input("Anna putken säde:\n"))
        pipe_length = float(input("Anna putken pituus:\n"))

        result = pipe_volume(pipe_radius, pipe_length)
        print(f"Putken tilavuus: {result} m3")
        print()

    if choice == 0:
        print("Kiitos ohjelman käytöstä!")
        break