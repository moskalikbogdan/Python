"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

import math

fun = list(input('''Aby obliczyć miejsca zerowe swojej funkcji kwadratowej wprowadź ją w formacie ax^2+bx+c:
 '''))
a = 0
b = 0
c = 0
n = fun.index('^')

for j in range(0,n-1):
    if fun[n-2-j] == "-":
        a = a * (-1)
    else:
        a = a + int(fun[n-2-j])*10**j
    
fun[n-1] = 0
m = fun.index('x')

for i in range(0, m-(n+3)):
    b = b + int(fun[m-1-i])*10**i
if fun[n+2] == "-":
    b = b * (-1)
    
for i in range(0, (len(fun)-1)-(m+1)):
    c = c + int(fun[len(fun)-1-i])*10**i    
if fun[m+1] == "-":
    c = c * (-1)
    
if b*b-4*a*c < 0:
    print('''Twoja funkcja nie posiada miejsc zerowych''')
    
else:
    
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    
    print('''Miejsca zerowe twojej funkcji to:
    x1 = ''',x1,'''
    x2 = ''',x2)
        
    if x1 == x2: 
        print('Tylko jedno miejsce zerowe!')