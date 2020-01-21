"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""
print ('''Program wyliczy sumę n kolejnych liczb tego ciągu. 
Wprowadż liczby ciągu. Podaj pierwszą:''')

a = int(input())
b = int(input('Podaj drugą liczbę:'))

def suma(a,b):
    suma=0

    for i in range(a,b+1):
        suma = suma + i
    return suma

print('Suma ciągu liczb to:', suma(a,b))