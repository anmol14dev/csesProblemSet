import math

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    elif n % 2 == 0:
        print(2)
    else:
        print(3)
