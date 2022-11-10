text = input("Anna jokin teksti:\n")

text_r = text[::-1]

if text == "":
    print("Antamasi teksti on tyhjä.")
elif text == text_r:
    print(f"{text_r}\nPalindromi: KYLLÄ")
else:
    print(f"{text_r}\nPalindromi: EI")
