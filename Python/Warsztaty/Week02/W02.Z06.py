print('Podaj który n-ty element ciągu Fibonnaciego kchcesz poznać:')
a = int(input())

def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        nowy = 0
        x = [1,1]
        for i in range(2,n):
            nowy=x[i-1] + x[i-2]
            x.append(nowy)
        return x[n-1]

print('Ten element ciągu to:', (fib(a)))
numbers =[1,1]

def fib2(numbers):
    
    new = 0
    for i in range(a-2):                  
        new = numbers[-1] + numbers[-2]  
        numbers.append(new)              
        print (new)                        
        
print('''1
1''')
fib2(numbers)