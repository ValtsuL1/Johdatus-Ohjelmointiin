movies = [
    {"name": "Komisario Palmun Erehdys", "year": "1960"},
    {"name": "Kauas pilvet karkaavat", "year": "1996"},
    {"name": "Mies vailla menneisyyttä", "year": "2002"},
    {"name": "Yksin marsissa", "year": "2015"},
    {"name": "Rita Hayworth – avain pakoon", "year": "1994"},
    {"name": "Interstellar", "year": "2014"}
]

movies_new = []
movies_old = []

for movie in movies:
    year = int(movie["year"])
    if year >= 2000:
        movies_new.append(movie["name"])
    else:
        movies_old.append(movie["name"])

movies_new = ", ".join(movies_new)
movies_old = ", ".join(movies_old)

print(f"Seuraavat elokuvat on julkaistu 2000-luvulla:\n{movies_new}")
print(f"Seuraavat elokuvat on julkaistu ennen vuotta 2000:\n{movies_old}")
