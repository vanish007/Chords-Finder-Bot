from time import sleep

def fibonacci(a: int = 0, b: int = 1):
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
ans = int(input())
for num, x in enumerate(fibonacci()):
    if num == ans:
        print(x)
        break

# iterator1 = iter(fibonacci())
# iterator2 = iter(enumerate(fibonacci()))
# while True:
#     item1, item2 = next(iterator1), next(iterator2)
#     print(item2)
#     sleep(1)
#     if item2 == ans:
#         print(item2)
#         break
