months = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu",
          "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu",
          "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

# pyydetään käyttäjältä monennenko kuukauden haluavat tulostaa
# vähennetään yksi että täsmää oikeassa elämässä
choice = int(input("Anna kuukauden numero:\n")) - 1

print(months[choice])
