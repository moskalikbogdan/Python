#W1 Zadanie 1
#Napisz skrypt, który będzie wyświetlać wszystkie kolejne dzielniki wprowadzonej liczby

"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""
    
a = int(input('Podaj liczbę, dla której wyliczę dzielniki'))
z = list()

for i in range(1,a+1):
    if a % i == 0:
        z.append(i)
    
print('dzielniki liczby to: ',a,' to: ',z)