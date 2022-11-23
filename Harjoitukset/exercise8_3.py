from PIL import Image, ImageDraw, ImageFont

# luo listan kolmesta pääväristä
colors = [
    # 1. Punainen
    (255, 0, 0),
    # 2. Vihreä
    (0, 255, 0),
    # 3. Sininen
    (0, 0, 255)
]

# ilmoittaa käyttäjälle mikä numero vastaa mitä väriä
print("1 = Punainen, 2 = Vihreä, 3 = Sininen")
print()

# tallentaa numeron jokaiselle elementille, väri saadaan colors listasta
bg_color = int(input("Anna taustaväri:\n")) - 1
text_color = int(input("Anna tekstin väri:\n")) - 1
triangle_color = int(input("Anna kolmion väri:\n")) - 1
circle_color = int(input("Anna ympyrän väri:\n")) - 1

# luo muuttujan jossa on piirrettävän kuvan atribuutit
# kaikki värit kuvan elementeille on käyttäjän valitsemia
img = Image.new("RGB", (500, 300), color=(colors[bg_color]))

# asettaa font muuttujaan arial fontin, kooksi 16 pistettä
font = ImageFont.truetype("arial.ttf", 16)

# sana joka tulee kuvaan
word = "Postikortista päivää!"

# luo piirto-olion
d = ImageDraw.Draw(img)

# piirtää tekstin kuvaan, fontti tulee font muuttujasta, sana word muuttujasta
d.text((40, 250), word, fill=(colors[text_color]), font=font)

# piirtää kolmion
d.polygon([(300, 250), (200, 100), (400, 100)], fill=(colors[triangle_color]))

# piirtää ympyrän kolmion sisälle
d.ellipse((250, 103, 350, 203), fill=(colors[circle_color]), outline=(colors[circle_color]))

# tallentaa kuvan png muodossa
img.save("picture123.png")
