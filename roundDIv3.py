t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    previndex = [int(0) for _ in range(1, n + 1)]
    count = [int(0) for _ in range(1, n + 1)]
    s = set(l)
    if len(s) <= 2:
        if len(s) == 1:
            print(0)
        else:
            print(1)
    else:
        for i in range(n):
            number = l[i]
            if i - previndex[number - 1] > 1:
                count[number - 1] += 1
            previndex[number - 1] = i
        for i in range(n):
            if previndex[i] != 0 and ((n - 1 - previndex[i]) > 0):
                count[i] += 1
            if previndex[i] == 0:
                count[i] = n + 1
        count.sort()
        print(count[0])
