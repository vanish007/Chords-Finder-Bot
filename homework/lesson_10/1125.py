from time import sleep

def squares(n = 1):
    while True:
        yield n**2
        n += 1


iterator = iter(squares())
t = int(input())
while True:
   item = next(iterator)
   if item <= t:
       print(item, end=' ')
   else:
       break
