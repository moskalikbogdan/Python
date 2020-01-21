import numpy as np

print('''Policzę srednią i odchylenie standardowe z listy którą wprowadzisz
      Z ilu elementów ma się składać lista?:
    ''')
a = int(input())

print('''Wprowadź pojedyńczo elementy twojej listy:''')
x = []

for i in range(0,a):
    x.append(int(input('Wprowadź element %i:'%(i+1))))


def srednia(x):
    suma = 0
    for i in range(len(x)):
        suma = suma + x[i]
    return suma/len(x)   

def stOdchylenie(x):
    suma = 0
    for i in range(len(x)):
        sr = srednia(x)
        suma = suma + (x[i] - sr)**2
    return round((suma/len(x))**(1/2),2)


print ()
print('Średnia twojej listy to:')
print(srednia(x))
print('Odchylenie standardowe twojej listy to:')
print(stOdchylenie(x))