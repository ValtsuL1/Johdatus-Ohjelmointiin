first_names = ["Macadamia", "Sipuliina", "Leo", "Eino", "Oliver", "Elias", "Onni", "Väinö", "Noel",
               "Eeli", "Toivo", "Leevi", "Joel", "Eetu", "Benjamin", "Viljami", "Hugo"]

# katsoo että ei ole e tai iso E
first_names_new = [x for x in first_names if "e" not in x]
first_names_new = [x for x in first_names_new if "E" not in x]
# katsoo että ei ole s tai iso S
first_names_new = [x for x in first_names_new if "s" not in x]
first_names_new = [x for x in first_names_new if "S" not in x]
# katsoo onko pituus alle 8 merkkiä
first_names_new = [x for x in first_names_new if len(x) < 8]

# tulostaa jäljelle jääneet nimet allekkain
for x in first_names_new:
    print(x)
