text_to_convert = input("Syötä numero tai teksti:\n")


def convert_num_to_text(text):
    text_length = len(text)
    if text_length <= 5:
        text = text.replace("1", "yksi ")
        text = text.replace("2", "kaksi ")
        text = text.replace("3", "kolme ")
        text = text.replace("4", "neljä ")
        text = text.replace("5", "viisi ")
        text = text.replace("6", "kuusi ")
        text = text.replace("7", "seitsemän ")
        text = text.replace("8", "kahdeksan ")
        text = text.replace("9", "yhdeksän ")
        text = text.replace("0", "nolla ")
        print(text)
    else:
        print("Liian monta numeroa!")


def convert_text_to_num(text):
    text_length = text.count(" ") + 1
    if text_length <= 5:
        text = text.replace("yksi", "1")
        text = text.replace("kaksi", "2")
        text = text.replace("kolme", "3")
        text = text.replace("neljä", "4")
        text = text.replace("viisi", "5")
        text = text.replace("kuusi", "6")
        text = text.replace("seitsemän", "7")
        text = text.replace("kahdeksan", "8")
        text = text.replace("yhdeksän", "9")
        text = text.replace("nolla", "0")
        text = text.replace(" ", "")
        print(text)
    else:
        print("Liian monta sanaa!")


# jos vaihdetaan numero tekstiksi, laskee merkkejen määrän
# jos merkkejä on alle viisi, vaihtaa numerot tekstiksi, ja tulostaa
if text_to_convert.isnumeric():
    convert_num_to_text(text_to_convert)

# jos vaihdetaan teksti numeroiksi, laskee välilyönnit ja lisää yhden
# tällä saadaan numeroiden määrä
# jos numeroita on alle viisi, vaihtaa tekstin numeroiksi
# lopussa poistaa välilyönnit ja tulostaa
else:
    convert_text_to_num(text_to_convert)
