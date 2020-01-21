"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""
a = list(input("Wprowadź swoje zdanie:"))
zdOdwrocone = list()
    
for i in reversed(range(0,len(a))):
    print(a[i])
    zdOdwrocone.append(a[i])
    
print(' '.join(zdOdwrocone))