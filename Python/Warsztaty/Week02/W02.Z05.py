


print('Wprowadź podstawę silni:')
a = int(input())

def silniaRekur(n):
    if n == 1:
        return 1

    else:
        return n * silniaRekur(n-1)
    
def silniaIter(n):
    silnia = 1
    for i in range(1,n+1):
        silnia = silnia * i
    return silnia

print('Rekurencyjne wyszło:', (silniaRekur(a)))
print('Iteracyjnie wyszło:', (silniaIter(a)))