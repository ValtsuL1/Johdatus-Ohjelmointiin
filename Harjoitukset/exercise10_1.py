def read_content():
    # asettaa file_handle muuttujaan artist.txt tiedoston sisällön luku-oikeuksilla
    file_handle = open("artists.txt", "r", encoding="UTF-8")
    content = file_handle.read()
    file_handle.close()
    # tekee content muuttujan riveistä listan
    lines = content.split("\n")
    for line in lines:
        print(f"-> {line}")


read_content()
