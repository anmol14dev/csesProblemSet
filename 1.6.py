s = input()
l = len(s)
freq = dict()
for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
count = 0
for i in freq:
    if freq[i] % 2 != 0:
        count += 1
if count > 1:
    print("NO SOLUTION")
else:
    s = ""
    char_odd = ""
    for i in freq:
        if freq[i] % 2 != 0:
            char_odd = i
            freq[i] = freq[i] - 1
        for j in range(0, freq[i] // 2):
            s = s + i
    s_revrse = s[::-1]
    s = s + char_odd
    s = s + s_revrse
    print(s)
