"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

from time import sleep as delay

print('''Ten program liczy do miliona,
chyba że przyciśniesz CTRL+C :)''')
i = 0
try:
    while True:
        i = i+1
        print(i)
        delay(1)
except KeyboardInterrupt:
    pass