def repititions():
    s = input()
    count = 1
    prev = s[0]
    m = 0
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            m = max(m, count)
            count = 1
            prev = s[i]
    m = max(m, count)
    print(m)


repititions()