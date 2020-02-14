"""
@author: Bogdan Moskalik, gr. 2 niestacjonarne, DataScience
"""
#%%
# Zad. 3. Utwórz skrypt do zamiany kilometrów na mile i na odwrót
	

a = int(input('''Jeśli chcesz zamienić kilometry na mile wpisz 1
              Jeśli chcesz zamienić mile na kilometry wpisz 2
	'''))
	

if a == 1:
    n = float(input('''Wprowadź wartość kilometrów które chcesz zamienić na mile'''))
    print(n,' kilometrów to ',n*0.62137,' mil' )
else:
    n = float(input('''Wprowadź wartość mil które chcesz zamienić na kilometry'''))
    print(n,' mil to ',n/0.62137,' kilometrów' )

#%%
# Zad 7. Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika 
# zdanie i wyświetli w kolejnych wierszach litery tego zdania w odwróconej 
  #kolejności
  
a = list(input('''Wprowadź swoje zdanie:
'''))
aOdwr = list()
    
for i in reversed(range(0,len(a))):
    print(a[i])
    aOdwr.append(a[i])
    
print(' '.join(aOdwr))

#%%
# Zad 8. W klasie przeprowadzono sprawdzian, za który uczniowie mogli otrzymać maksymalnie 40 punktów. 
# Skala ocen w szkole jest następująca: 0-39% - ndst, 40-49% - dop, 50-69% - dst, 70-84% - db, 
# 85-99% - bdb, 100% - cel. Utwórz skrypt z interfejsem tekstowym, który na podstawie podanej 
#liczby punktów ze sprawdzianu wyświetli ocenę jaka się należy (skorzystaj z konstrukcji if, elif, else)

a = float((input('''Podaj ile pkt. otrzymałeś na sprawdzanie:
''')))*2.5
    
if a <= 39:
    print('Twoj ocena to ndst')
elif a <= 49:
    print('Twoj ocena to dop')
elif a<= 69:
    print('Twoja ocena to dst')
elif a<= 84:
    print('Twoja ocena to db')
elif a<= 99:
    print('Twoja ocena to bdb')
else:
    print('Twoja ocena to cel')    


#%%
# zad. 11. Utwórz krypt z interfejsem tekstowym który obliczy silnię od danego argumentu. 
# Wykonać zadanie na dwa sposoby – iteracyjnie i rekurencyjnie
    
print('Wprowadź podstawę silni:')
a = int(input())


def silniaRekur(n):
    if n == 1:
        return 1


    else:
        return n * silniaRekur(n-1)
    
def silniaIter(n):
    silnia = 1
    for i in range(1,n+1):
        silnia = silnia * i
    return silnia


print('Rekurencyjne wyszło:', (silniaRekur(a)))
print('Iteracyjnie wyszło:', (silniaIter(a)))

#%%
# Zad. 12. Utworzyć skrypt z interfejsem tekstowym obliczający n-ty element ciągu Fibonacciego 
# – wykonać zadanie iteracyjnie i rekurencyjnie


print('Podaj który n-ty element ciągu Fibonnaciego kchcesz poznać:')
a = int(input())
	

def fiboRekur(n):
    if (n == 1) or (n == 2):
        return 1
	
    else:
        return fiboRekur(n-1) + fiboRekur(n-2)
	    
def fiboIter(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        x = [1,1]
        for i in range(2,n):
            x.append(x[i-1] + x[i-2])
        return x[n-1]

print('Rekurencyjne wyszło:', (fiboRekur(a)))
print('Iteracyjnie wyszło:', (fiboIter(a)))

#%%
# Zad. 13. Utworzyć skrypt z interfejsem tekstowym obliczający symbol Newtona n po k. 
# Utworzyć funkcję, która będzie wywoływać inną funkcję

print('Dzisiaj policzymy symbol Newtona n po k, liczby podane muszą być naturalne')
print('Podaj wartość n:')
n = int(input())
k = int(input())


def silnia(n):
    if n == 1:
        return 1


    else:
        return n * silniaRekur(n-1)
    
def symbolNewtona(n,k):
    if (n>=k) and (k>=0):
        wynik = silnia(n)/((silnia(k)*silnia(n-k)))
        return wynik
    else:
        print('Wprowadziłeś dane niezgodne z założeniem')


print('n po k dla twoich liczb wynosi:')
print(symbolNewtona(n,k))

#%%
# Zad. 22. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie mediana (skorzystaj z metody sort działającej na standardowych listach)

def calcMed(a):
	    a.sort()
	    if len(a)%2 == 0:
	        med = (a[int(len(a)/2-1)] + a[(int(len(a)/2))])/2
	    else:
	        med = a[int(len(a)/2 - 0.5)]
	        
	    return med

#%%
# Zad. 24. Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie odchylenie standardowe średniej


x = list()
	

print('Wpisz ile elementów listy chcesz wprowadzić:')
a = int(input())
	

print('''Teraz po kolei, pojedyńczo wprowadzaj elementy listy.
	Program wyliczy średnią i odchylenie standardowe twojej listy:''')
	
	

	

for i in range(0,a):
	    x.append(int(input('Wprowadź element %i: ' %(i+1))))
	

def calcMean(x):
	    suma = 0
	    for i in range(len(x)):
	        suma = suma + x[i]
	    return suma/len(x)   
	

def calcStdDev(x):
	    suma = 0
	    for i in range(len(x)):
	        sr = calcMean(x)
	        suma = suma + (x[i] - sr)**2
	    return round((suma/len(x))**(1/2),2)
	

print()
print('Średnia twojej listy to:')
print(calcMean(x))
print('Odchylenie standardowe twojej listy to:')
print(calcStdDev(x))

#%%
# 26. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, 
# a jej wynikiem będzie trzeci moment centralny (skośność)

def calcSkos(x):
    suma = 0
    sr = calcMean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**3
    return ((suma/len(x))*(1/calcStdDev(x)**3))

#%%
# Zad 27. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych,
# a jej wynikiem będzie czwarty moment centralny (kurtoza)

import numpy as np

def odchylenie(x):
    xMean = np.mean(x)
    stdSuma = 0
    for i in range(len(x)):
        stdSuma = stdSuma + (x[i] - xMean)**2
    stdSuma = stdSuma/len(x)
    return np.sqrt(stdSuma)

def calcKurt(x):
    suma = 0
    sr = np.mean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**4
    return (((1/odchylenie(x)**4)*(suma/len(x)))-3)

#%%
# Zad 35. Utwórz klasę Prostokąt, a następnie na jej podstawie (korzystając z 
#           mechanizmu dziedziczenia) utwórz klasę Kwadrat

# tworzę klasę prostokąta
class ProstyProstokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def obwod (self):
        return 2*self.a+2*self.b

    def pole (self):
        return self.a*self.b

# pytam się o wymiary prostokąta
        
print ('podaj długosc boku A')
BokA = int(input())
print ('podaj długosc boku B')
BokB = int(input())
        
x = ProstyProstokat (BokA,BokB)
print ("Obwód Prostrojąta wynosi", x.obwod())
print ('Pole Prostokąta wynosi', x.pole())

# po przez dziedziczenie klas tworzę klasę kwadrat
class ProstyKwadrat(ProstyProstokat):
    def __init__(self, a):
        super().__init__(a, a)

y = ProstyKwadrat (BokA)
print ("Obwód Kwadratu wynosi", y.obwod())
print ('Pole kwadratu wynosi', y.pole())
