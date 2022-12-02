def sec_word(word, number):
    # tekee käyttäjän antaman sanan jokaisesta merkistä listan
    # tekee myös valmiiksi tyhjän listan uudelle merkkijonolle
    word_list = list(word)
    word_list_new = []

    amount = len(word_list)

    for index in range(amount):
        # hakee merkin sijoitusluvun char_index muuttujaan
        char_index = ord(word_list[index])
        # hakee char muuttujaan merkin char_index luvusta johon
        # on lisätty käyttäjän antama siirtoluku
        char = chr(char_index + number)
        # lisää uuden merkin aiemmin luotuun tyhjään listaan
        word_list_new.append(char)

    # liittää listan merkit yhteen .join funktiolla
    # muuttaa myös merkit string muotoon
    word_new = "".join(str(x) for x in word_list_new)
    return word_new


word = input("Anna sana:\n")

number = int(input("Anna siirtoluku:\n"))

word_new = sec_word(word, number)

# tulostaa "salatun" sanan
print(word_new)
