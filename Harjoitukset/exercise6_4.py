products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y82018_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

year = input("Minkä vuoden koodit haetaan?\n")

amount = len(products)

for index in range(amount):
    # luo text muuttujan listan elementistä
    text = products[index]
    # luo parts listan joka koostuu halkaistusta text muuttujasta
    parts = text.split("_")
    # jos parts muuttujan 2. osa on sama kuin käyttäjän antama
    # year muuttuja, tulostaa parts muuttujan 1. osan
    if year == parts[1]:
        print(parts[0])
