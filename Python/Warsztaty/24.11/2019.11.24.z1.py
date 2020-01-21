"""
@author: Bogdan Moskalik, 
DataScience, 
Niestacjonarne, 
Grupa 2
"""

from matplotlib import pyplot as plt


def quadratic_data(a, b, c):
    xaxis = []
    yaxis = []
    for x in range(0, 100):
        xaxis.append(x)
        yaxis.append(a*(x**2) + b*x + c)
        
    return xaxis, yaxis

x, y = quadratic_data(2, 5, 1)
plt.plot(x, y)