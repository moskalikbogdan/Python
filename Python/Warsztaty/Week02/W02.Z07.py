"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

print('Dzisiaj policzymy symbol Newtona n po k, gdzie n>=k oraz k>=0')
print('Podaj wartość n:')
n = int(input())
print('Podaj wartość k:')
k = int(input())

def silnia(n):
    x = 1
    for i in range(x, n + 1):
        x = x * i
    return x
    
def symbolNewtona(n,k):
    if (n>=k) and (k>=0):
        sn = silnia(n)/((silnia(k)*silnia(n-k)))
        return sn
    else:
        print('Dla tych liczb nie obliczę symbolu Newtona')

print('Symbol Newtona to:')
print(symbolNewtona(n,k))