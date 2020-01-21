"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

print('''Sprawdzę czy twoja liczba jest ujemna czy dodatnia''')


a = float(input('Wprowadź liczbę:'))
if a == 0:
            print('Zero')
elif a > 0:
            print('Liczba dodatnia')
else:
            print('Liczba ujemna')