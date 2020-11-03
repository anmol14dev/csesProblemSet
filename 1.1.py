def WierdAlgo(n):
    print("{} ".format(n), end="")
    if n == 1:
        print()
    elif n % 2 == 0:
        WierdAlgo(n // 2)
    else:
        WierdAlgo((n * 3) + 1)


n = int(input())
WierdAlgo(n)