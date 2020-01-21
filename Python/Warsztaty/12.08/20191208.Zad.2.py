#Utwórz klasę Prostokąt, a następnie na jej podstawie 
#(korzystając z mechanizmu dziedziczenia) utwórz klasę Kwadrat
"""
@author: Bogdan Moskalik, gr. 2 niestacjonarne, DataScience
"""

# tworzę klasę prostokąta
class ProstyProstokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def obwod (self):
        return 2*self.a+2*self.b

    def pole (self):
        return self.a*self.b

# pytam się o wymiary prostokąta
        
print ('podaj długosc boku A')
BokA = int(input())
print ('podaj długosc boku B')
BokB = int(input())
        
x = ProstyProstokat (BokA,BokB)
print ("Obwód Prostrojąta wynosi", x.obwod())
print ('Pole Prostokąta wynosi', x.pole())

if BokA==BokB:
    print ('Ten prostokąt to również kwadrat')

# po przez dziedziczenie klas tworzę klasę kwadrat
class ProstyKwadrat(ProstyProstokat):
    def __init__(self, a):
        super().__init__(a, a)

y = ProstyKwadrat (BokA)
print ("Obwód Kwadratu wynosi", y.obwod())
print ('Pole kwadratu wynosi', y.pole())