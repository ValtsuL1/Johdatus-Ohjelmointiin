from functions import show_numbered_list

participants_string = input("Syötä tapahtumaan osallistujat pilkulla eroteltuina:\n")

# tekee participants merkkijonosta listan, joka koostuu kokonimistä
participants = participants_string.split(",")
# poistaa alusta ja lopusta ylimääräiset välilyönnit
participants = [p.strip() for p in participants]

# kutsuu show_numbered_list funktion, tulostaa title parametrin
# ja participants listan elementit
show_numbered_list("Ilmoittautumisjärjestys:", participants)

# järjestää listan elementit aakkosjärjestykseen
participants.sort()

# kutsuu funktion taas, tällä kertaa aakkosjärjestyksessä
show_numbered_list("Aakkosjärjestys etunimen perusteella:", participants)

# muuttaa listan nimien etunimen ja sukunimen paikan ja järjestää
participants = [" ". join(reversed(p.split(" "))) for p in participants]
participants.sort()

# kutsuu funktion, järjestettynä sukunimen perusteella
show_numbered_list("Aakkosjärjestys sukunimen perusteella:", participants)
