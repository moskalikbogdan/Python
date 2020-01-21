"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

a = int(input('''Jeśli chcesz zamienić kilometry na mile wpisz 1
Jeśli chcesz zamienić mile na kilometry wpisz 2
'''))

if a == 1:
    n = float(input('''Wprowadź wartość kilometrów które chcesz zamienić na mile
'''))
    print(n,' kilometrów to ',n*0.62137,' mil' )
else:
    n = float(input('''Wprowadź wartość mil które chcesz zamienić na kilometry
'''))
    print(n,' mil to ',n/0.62137,' kilometrów' )