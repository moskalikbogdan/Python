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
