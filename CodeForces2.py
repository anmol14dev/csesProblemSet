t = int(input())
for i in range(t):
    n, q = [int(x) for x in input().split()]
    s = input()
    for _ in range(q):
        l, r = [int(x) for x in input().split()]
        firstChar = s[l - 1]
        lastChar = s[r - 1]
        indexF = n
        indexL = -1
        for i in range(n):
            if s[i] == firstChar:
                indexF = i
                break
        for i in range(n - 1, -1, -1):
            if s[i] == lastChar:
                indexL = i
                break

        if indexF < l - 1 or indexL > r - 1:
            print("YES")
        else:
            print("NO")
