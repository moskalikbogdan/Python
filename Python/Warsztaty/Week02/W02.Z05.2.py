"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

n = int(input("Prosze podac liczbe: "))

def silnia_rek(n):
    if n>1:
        return n*silnia_rek(n-1)    
    elif n in (0,1):
        return 1;
 
def silnia_iter(n):

    silnia=1 
    if n in (0,1):  
        return 1
    else:
        for i in range(2,n+1):  
            silnia = silnia*i
        return silnia
 
print ('silnia rekurencyjnie', silnia_rek(n))
print ('silnia iteracyjnie', silnia_iter(n))