import os

slownik = {}
#sPlik = open("slownik.txt")
sPlik="slownik.txt"
haslo = set()


def otworz(plik):
    if os.path.isfile(sPlik):
        with open(sPlik, "r") as pliktxt:
            for line in pliktxt:
                t = line.split(":")
                haslo = t[0]
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")
                slownik[haslo] = znaczenia
    return len(slownik)


def zapisz(slownik):
    pliktxt = open(sPlik, 'w')
    print(slownik)
    for haslo in slownik:
        znaczenia = ",".join(slownik[haslo])
        linia = ":".join([haslo, znaczenia])
        pliktxt.write(linia+'\n')
    pliktxt.close()


def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str


otworz(sPlik)
print("""Podaj dane w formacie:
Hasło: znaczenie
Aby zakończyć wprowadzanie danych, podaj finit.
    """)
nowy = False
while True:
    dane = input("Podaj hasło i znaczenie: ")
    t = dane.split(":")
    haslo = t[0].strip().lower()
    if haslo == 'finit':
        break
    elif dane.count(":") == 1:
        if haslo in slownik:
            print("Wyraz", haslo, " i jego znaczenia są już w słowniku.")
            op = input("Zastąpić wpis (t/n)? ")
        if haslo not in slownik or op == "t":
            print(t[1])
            znaczenia = t[1].split(",")
            znaczenia = list(map(oczysc, znaczenia))  # oczyszczamy listę
            slownik[haslo] = znaczenia
            nowy = True
        else:
            print("Błędny format!")

if nowy: zapisz(slownik)

print("=" * 50)
print("{0: <15}{1: <40}".format("Hasło", "Znaczenia"))
print("=" * 50)
for haslo in slownik:
    print("{0: <15}{1: <40}".format(haslo, ",".join(slownik[haslo])))