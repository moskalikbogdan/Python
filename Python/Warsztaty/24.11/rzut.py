
import matplotlib.pyplot as plt
import math

def wykres(x, y):
    plt.plot(x, y)
    plt.xlabel('os-x')
    plt.ylabel('os-y')
    plt.title('Zadanie2 - rzut ukosny')
    
def frange(start, koniec, interval):
    numbers = []
    while start < koniec:
        numbers.append(start)
        start = start + interval
        
    return numbers

def kat_rzutu(u, kat):
    
    kat = math.radians(kat)
    g = 9.81
    
    trajektoria = 2*u*math.sin(kat)/g

    intervals = frange(0, trajektoria, 0.001)
    
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(kat)*t)
        y.append(u*math.sin(kat)*t-0.5*g*t*t)
        
    print('Time of flight: {0}'.format(trajektoria)) 
    print('Max horizontal distance: {0}'.format(max(x)))
    print('Max vertical distance: {0}'.format(max(y)))

    wykres(x, y)
    
if __name__ == '__main__':
    num_traj = int(input('Jak dużo rzutów? '))
    for i in range(num_traj):
        try:
            u = float(input('Podaj prędkosc rzutu (m/s): '))
            kat = float(input('Podaj kąt rzutu (w stopniach): '))
        except ValueError:
            print('Wprowadziłes błędne dane')
        else:
            kat_rzutu(u, kat)
    
    plt.show()