import numpy as np
import collections as cl
from math import sqrt
import matplotlib as mpl

#ZAD1
def calcMean(a):
    return sum(a)/len(a)

#ZAD2
def calcMed(a):
    a.sort()
    if len(a)%2 == 0:
        med = (a[int(len(a)/2-1)] + a[(int(len(a)/2))])/2
    else:
        med = a[int(len(a)/2 - 0.5)]
        
    return med

#ZAD3
def calcDomin(x):
    return cl.Counter(x).most_common()[0][0]

#ZAD4
def calcStdDev(x):
    suma = 0
    sr = calcMean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**2
    return ((suma/len(x))**(1/2))

#ZAD5
def calcWari(x):
    suma = 0
    sr = calcMean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**2
    return (suma/len(x))

#ZAD6
def calcSkos(x):
    suma = 0
    sr = calcMean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**3
    return ((suma/len(x))*(1/calcStdDev(x)**3))

#ZAD7
def calcKurt(x):
    suma = 0
    sr = calcMean(x)
    for i in range(len(x)):
        suma = suma + (x[i] - sr)**4
    return (((1/calcStdDev(x)**4)*(suma/len(x)))-3)

#ZAD8
def calcKorel(x,y):
    if len(x) != len(y):
        return('Listy muszą mieć taką samą długość')
    else:
        sumaXY = 0
        sumaX = 0
        sumaY = 0
        sumaX2 = 0
        sumaY2 = 0
        
        for i in range(len(x)):
            sumaXY += x[i]*y[i]
            sumaX += x[i]
            sumaY += y[i]
            sumaX2 += x[i]**2
            sumaY2 += y[i]**2
            
        c1 = (len(x) * sumaXY - sumaX*sumaY)
        c2 = sqrt((len(x) * sumaX2 - sumaX**2)*(len(y) * sumaY2 - sumaY**2))
        
        return c1/c2

#ZAD9
def calcRegrs(x,y):
    if len(x) != len(y):
        return('Listy muszą mieć taką samą długość')
    else:
        sumaXY = 0
        sumaX = 0
        sumaY = 0
        sumaX2 = 0
        
        for i in range(len(x)):
            sumaXY += x[i]*y[i]
            sumaX += x[i]
            sumaY += y[i]
            sumaX2 += x[i]**2
            
        a = (len(x) * sumaX * sumaY - sumaX * sumaY)/(len(x) * sumaX2 - sumaX**2)
        b = (len(x) * sumaX2 * sumaY - sumaX * sumaXY)/(len(x) * sumaX2 - sumaX**2)
        
        return a,b
    
#ZAD10
def randomStats():
   a = np.random.standard_normal(size = 1000)
   mpl.pyplot.hist(a, 50, density=True, facecolor='g')
   print('Średnia: ', calcMean(a))
   print('Mediana: ', calcMed(a))
   print('Dominanta: ', calcDomin(a))
   print('Odchylenie standardowe: ', calcStdDev(a))
   print('Wariancja: ', calcWari(a))
   print('Skośność: ', calcSkos(a))
   print('Kurtoza: ', calcKurt(a))
   return a