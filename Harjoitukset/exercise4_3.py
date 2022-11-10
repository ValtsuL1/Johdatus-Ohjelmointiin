text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"

print(text)
print()

# vaihtaa sanan fox, sanaksi duck ja tulostaa
text = text.replace("fox", "duck")

print(text)
print()

# poistaa käyttäjän antaman sanan
# jos sanaa ei löydy, tekstiä ei tulosteta
# poistaa myös ylimääräiset väilyönnit
word = input("Anna poistettava sana:\n")
print()

if word in text:
    text = text.replace(word, "")
    text = text.replace("  ", " ")
    text = text.replace(" .", ".")
    text = text.replace(" !", "!")
    print(text)
else:
    print("Sanaa ei löytynyt.")
    print()

# laskee merkkien määrän ja tulostaa
text_length = len(text)

print(f"Merkkejä: {text_length}")
print()

# sanojen määrä saadaan laskemalla välilyönnit yhteen ja lisäämällä yhden
word_count = text.count(" ") + 1

print(f"Sanoja: {word_count}")
print()

# vaihtaa pisteet rivinvaihdoiksi
text = text.replace(".", "\n")

print(text)
print()

usertext = input("Anna jokin lause:\n")
usertext_length = len(usertext)

if usertext_length <= 20:
    print(usertext)
elif usertext_length > 20:
    usertext = usertext[0:20] + "..."
    print(usertext)
