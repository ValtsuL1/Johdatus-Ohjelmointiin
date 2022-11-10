products = ["PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
            "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
            "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
            "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
            "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
            "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"]

categories = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

# laskee montako tuotetta on listassa
amount = len(products)

for index in range(amount):
    # luo text muuttujan, joka muuttuu vuorotellen jokaiseksi
    # products listan elementiksi
    text = products[index]
    # luo parts listan, joka koostuu text muuttujasta
    # pilkotuista osista
    parts = text.split("_")
    # asettaa muuttujille arvot parts listasta
    producer = parts[0]
    name = parts[1]
    model = parts[2]
    year = parts[3]
    month = parts[4]
    day = parts[5]
    # kategoria saadaan muuttamalla parts[7] numeroksi
    # ja hakemalla categories listasta elementti vastaavalla luvulla
    category = categories[int(parts[7])]
    # tulostaa lopuksi tuotteen tiedot
    print(f"Valmistaja: {producer}\n"
          f"Nimi ja malli: {name} ({model})\n"
          f"Kategoria: {category}\n"
          f"Lisäyspäivämäärä: {day}.{month}.{year}\n")
