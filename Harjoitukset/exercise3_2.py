temperature = input("Syötä päivän lämpötila: ")
temperature = int(temperature)

if temperature >= 0 and temperature <= 10:
    print("KYLMÄÄ")
if 11 <= temperature <= 15:
    print("KOLEAA")
if temperature >= 16 and temperature <= 20:
    print("NORMAALI LÄMPÖTILA")
if temperature >= 21 and temperature <= 25:
    print("LÄMMINTÄ")
if temperature >= 26 and temperature <= 30:
    print("HELLETTÄ")