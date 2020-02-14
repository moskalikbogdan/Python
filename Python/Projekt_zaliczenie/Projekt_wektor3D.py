import numpy

class Vector3D():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # moduł wektora |a|
    def modul(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    # współrzędne wektora a = [i, j, k]
    def __repr__(self):
        out = str(self.x) + "i "
        out += "+ "
        out += str(self.y) + "j "
        out += "+ "
        out += str(self.z) + "k"
        return "["+out+"]"
    
    # suma dwóch wektorów
    def __add__(self, sec):
        x = self.x + sec.x
        y = self.y + sec.y
        z = self.z + sec.z
        return Vector3D(x, y, z)
    
    # odejmowanie wektorów
    def __sub__(self, sec):
        x = self.x - sec.x
        y = self.y - sec.y
        z = self.z - sec.z
        return Vector3D(x, y, z)
    
    
    # mnożenie wektora przez liczbę
    def __mul__(self, liczba):
        x = self.x * liczba
        y = self.y * liczba
        z = self.z * liczba
        return Vector3D(x, y, z)
    
    # iloczyn skalarny
    def __xor__(self, sec):
        return self.x*sec.x + self.y*sec.y + self.z*sec.z
    
    # iloczyn wektorowy wektorów
    def __matmul__(self, sec):
        x = self.y * sec.z - self.z * sec.y
        y = self.z * sec.x - self.x * sec.z
        z = self.x * sec.y - self.y * sec.x
        return Vector3D(x, y, z)
        
if __name__ == "__main__":         
    
    # liczba do mnożenia 
    x = 2
    # puste wektory
    wektor1 = None
    wektor2 = None
    wektor3 = None

  # podane wektory
    wektor1 = Vector3D(5,4,3)
    wektor2 = Vector3D(2,1,6)
    wektor3 = Vector3D(7,8,9)
    
    # Przykładowe użycie zdefiniowanych operacji na wektorach
print("\nWektor a o współrzędnych    a = " + str(wektor1))
print("\nDługosć wektora v      |a| = " +str(wektor1.modul()))
print("\nWektor b o współrzędnych   b = " + str(wektor2))
print("\nDługosć wektora u      |b| = " +str(wektor2.modul()))
print("\nDodawanie wektorów   v + u = " + str(wektor1 + wektor2))
print("\nOdejmowanie wktorów  a - b = " + str(wektor1 - wektor2))
print("\nMnożenie wektora przez liczbę   " + str(x) + " x a = " + str(wektor1 * x))
print("\nIloczyn skalarny wektrów a i b = " + str(wektor1 ^ wektor2))
print("\nIloczyn wektorowy wektorów   a i b = " + str(wektor1 @ wektor2))
  
  # Iloczyn mieszany wektorów
print("\nwykorzystany Wektor c do iloczynu mieszanego o współrzędnych    c = " + str(wektor3))
print("\nIloczyn mieszany (a x b) ∘ c = " + str((wektor1 @ wektor2) ^ wektor3))