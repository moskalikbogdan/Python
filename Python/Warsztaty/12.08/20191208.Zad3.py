

class Animals:
    
   def __init__(self, wiek, waga, imie):
        self.wiek = wiek
        self.waga = waga
        self.imie = imie        
         

   def przedstaw(self):
        print ('Mam na imie', self.imie, 'mój wiek to:', self.wiek, 'kg', 'ważę', self.waga)
    
   def urodziny(self):
       print ('Będę miał', self.wiek+1, 'urodziny')      

class lew(Animals):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A tak w ogóle to jestem lwem")
        
class papuga(Animals):
    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor
        
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")

zwierze1 = Animals(23,'600kg', 'VanilaSky')
zwierze2 = lew(3, '150kg', 'Simba')
zwierze3 = papuga(2,'1,5kg', 'Emma', 'czerwona')  

zwierze1.przedstaw()
zwierze1.urodziny ()
zwierze2.przedstaw()
zwierze3.przedstaw()