def permutations():
    n = int(input())
    if n < 5:
        if n == 1:
            print(1)
        elif n == 2 or n == 3:
            print("NO SOLUTION")
        else:
            print("2 4 1 3")

    else:
        l = n // 2
        if n & 1 == 1:
            l += 1
        for i in range(1, l + 1):
            print("{} ".format(i), end="")
            if i + l <= n:
                print("{} ".format(i + l), end="")
        print()


permutations()
