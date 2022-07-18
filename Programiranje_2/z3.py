#Potrebno napisati regex koji
#vraca podudaranje ukoliko se unese string
#koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
#String mora sadržavati bar jedan broj između 0 i 5 i razmak.


import re

regex = "^j[0-5]+\s.*p$"

while 1:
    unos = input("Unesite ime:")
    rezultat = re.match(regex,unos)
    if rezultat:
        break
    else:
        print("Pogresan unos!")
print("Ispravan unos.")
