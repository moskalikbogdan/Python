"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

from numpy import lcm as np


wybor = int((input('''W tym programie możesz dodać 2 ułamki zwykłe!
Wybierz opcje wpisując odpowiednią cyfrę
1. Dowolne liczby. Wynik otrzymasz w postaci ułamka dziesiętnego
2. Wszystkie liczby są całkowite. Wynik otrzymasz w postaci ułamka zwykłego
''')))

if wybor == 1:
    dziel = list(input('''Wprowadz ułamki w postaci:a/b + c/d:
'''))
    print()
    
    num = [0.0,0.0,0.0,0.0]    
    licz = list()
    
    licz.append(dziel[:dziel.index('/')])
    licz.append(dziel[(dziel.index('/')+1):(dziel.index('+')-1)])
    del dziel[dziel.index('/')]
    licz.append(dziel[(dziel.index('+')+2):dziel.index('/')])
    licz.append(dziel[(dziel.index('/')+1):(len(dziel))])
    
    for i in range(0,4):
        try:
            a = licz[i].index('.')
            for m in range(0,a):
                num[i] = num[i] + float(licz[i][m])*10**(a-m-1)
            for n in range(a+1,len(licz[i])):
                num[i] = num[i] + float(licz[i][n])*10**((n-a)*(-1))
                num[i] = round(num[i], (len(licz[i])-licz[i].index('.')-1))
        except ValueError:
            for m in range(0,len(licz[i])):
                num[i] = num[i] + float(licz[i][m])*10**(len(licz[i])-m-1)
                
    wynik = num[0]/num[1] + num[2]/num[3]
    
    print("Twój wynik to: ",wynik)
else:
    dziel = list(input('''Wprowadz ułamki w postaci:a/b + c/d:
'''))
    print()
    
    num = [0,0,0,0]    
    licz = list()
    
    licz.append(dziel[:dziel.index('/')])
    licz.append(dziel[(dziel.index('/')+1):(dziel.index('+')-1)])
    del dziel[dziel.index('/')]
    licz.append(dziel[(dziel.index('+')+2):dziel.index('/')])
    licz.append(dziel[(dziel.index('/')+1):(len(dziel))])
    
    for i in range(0,4):
            for m in range(0,len(licz[i])):
                num[i] = num[i] + int(licz[i][m])*10**(len(licz[i])-m-1)
                
    
    z = np(num[1], num[3])
    for i in range(0,3,2):
        num[i] = num[i] * int((z/num[i+1]))
    num[0] = num[0] + num[2]
    print("Twój wynik to: ", num[0],"/",z)