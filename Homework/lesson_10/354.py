from time import sleep
from math import ceil

def prosto(n):
    while True:
        t = n
        for i in range(2, ceil(n**0.5)+1):
            if n % i == 0:
                yield i
                n //= i
                break
        if n == 1:
            break
        if t == n:
            yield n
            break
iterator = iter(prosto(int(input())))
while True:
    try:
        item = next(iterator)
        print(item,end='')
    except:
        print('\b ')
        break
    print('*', end='')
