
"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

a = float(input('Podaj temperaturę, którą chcesz zamienić: '))
print('''Wybierz jednostkę jaką chcesz uzyskać:
Jeśli chcesz uzyskać temperaturę w stopniach Celciusza wpisz 1
Jeśli chcesz uzyskać temperaturę w stopniach Fahrenheit'a wpisz 2''')
b = int(input())

if b == 1:
    c = (a-32)*(5/9)
    print('Twoja temperatura to ',c,'°C')
else:
    c = (a*9/5)+32
    print('Twoja temperatura to ',c,'°F')