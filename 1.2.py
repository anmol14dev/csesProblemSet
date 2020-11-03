def missingNumber():
    n = int(input())
    arr = [int(x) for x in input().split()]
    check = [int(0) for x in range(0, n)]
    for i in arr:
        check[i - 1] = -1
    for i in range(0, n):
        if check[i] != -1:
            print(i + 1)
            break


missingNumber()
