import os

slownik = {}  
sPlik = open("/slownik.txt")
haslo = set()

def otworz(plik):
    if os.path.isfile(sPlik):  
        with open('slownik.txt', "r") as pliktxt: 
            for line in pliktxt:  
                t = line.split(":")
                haslo = t[0]
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")
                slownik[haslo] = znaczenia
    return len(slownik)  
    pliktxt.close() 
    


def zapisz(slownik):
    pliktxt = open('slownik.txt', 'w')
    for haslo in slownik:
        znaczenia = ",".join(slownik[haslo])
        linia = ":".join([haslo, znaczenia])
        pliktxt.write(linia)  
    pliktxt.close()
 

print("""Podaj dane w formacie:
Hasło: znaczenie
Aby zakończyć wprowadzanie danych, podaj finit.
    """)

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
           znaczenia = t[1].split(",") 
           slownik[haslo] = znaczenia
           nowy = True
        else:
            print("Błędny format!")

if nowy: zapisz(slownik)

print ("="*50)
print ("{0: <15}{1: <40}".format("Hasło","Znaczenia"))
print ("="*50)
for haslo in slownik:
    print ("{0: <15}{1: <40}".format(haslo,",".join(slownik[haslo])))