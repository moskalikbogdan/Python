import numpy as np
import matplotlib.pyplot as plt

print('''podaj ile kategorii chcesz podać''')
a = int(input())

x = []

for i in range(0,a):
    x.append(input('Wprowadź nazwę kategorii %i:'%(i+1)))
print (x)
    

y = []

for i in range(0,a):
    y.append(int(input('Wprowadź wartosc pln na kategorie %i:'%(i+1))))
print (y)

etykiety = x
wartosci = y
plt.bar(etykiety, wartosci)
# możemy również zmienić np. kierunek tekstu etykiet słupków
plt.xticks(rotation=45)
plt.ylabel('wysokosc wydatków')
plt.xlabel('kategorie wydatków')
plt.show()