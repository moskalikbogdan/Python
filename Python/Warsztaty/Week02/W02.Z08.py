"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

import math

print('Wydrukujmy Trójką Paskala... ')

rows = int(input(' Podaj liczbę wierszy: '))

def newton(n, k):
    return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))

def pascal(rows):
    x = []
    for i in range(rows):
        wiersz = []
        for j in range(i + 1):
            wiersz.append(newton(i, j))
        x.append(wiersz)
    return x
    
    
for wiersz in pascal(rows):
    print (wiersz)