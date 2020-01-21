"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

print("Pomnożę liczbę wprowadzoną przez liczby od 1 do 10... ")
liczba=int(input("wprowadź liczbę: "))
for i in range(2, 11):
    i = i * liczba
print("This number: " + str(i) + " can be divide by: " + str(liczba))
print("Do you wish to continue?: ")
