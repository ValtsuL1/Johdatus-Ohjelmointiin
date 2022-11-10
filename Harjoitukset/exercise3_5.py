points = input("Anna pistemäärä: ")
points = int(points)

if points < 0 or points > 100:
    print("Pistemäärä ei ole mahdollinen.")

if 0 <= points <= 50:
    print("Arvosana: 0")
if 51 <= points <= 60:
    print("Arvosana: 1")
if 61 <= points <= 70:
    print("Arvosana: 2")
if 71 <= points <= 80:
    print("Arvosana: 3")
if 81 <= points <= 90:
    print("Arvosana: 4")
if 91 <= points <= 100:
    print("Arvosana: 5")
