"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

import numpy as np

print('''Policzę srednią i odchylenie standardowe z listy którą wprowadzisz
      Z ilu elementów ma się składać lista?:
    ''')
a = int(input())

print('''Wprowadź pojedyńczo elementy twojej listy:''')
x = []

for i in range(0,a):
    x.append(int(input('Wprowadź element %i:'%(i+1))))

print ()
print('Średnia twojej listy to:')
print(np.mean(x))
print('Odchylenie standardowe twojej listy to:')
print(round(np.std(x),2))