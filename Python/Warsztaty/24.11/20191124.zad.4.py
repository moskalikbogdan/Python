
"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

import matplotlib.pyplot as plt

def draw_fibo(n):
    ratio = []
    num = []

    a = 0
    b = 1    
    for i in range(1,n):
        c = a + b    
        num.append(i)
        ratio.append(c/b)
        a = b
        b = c
    draw_graph(num,ratio)
    
def draw_graph(x,y):
    plt.plot(x, y)
    plt.xlabel('Numery ciągu Fibonacciego')
    
    plt.ylabel('Ratio')
    plt.title('Stosunek między kolejnymi numerami Fibonacciego')

if __name__ == '__main__':
    draw_fibo(100)