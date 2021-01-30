n, m, k = [int(x) for x in input().split()]
desiredList = sorted([int(x) for x in input().split()])
size = sorted([int(x) for x in input().split()])
upperPointer, lowerPointer = 0, 0
count = 0
print(desiredList)
print(size)
while upperPointer < n and lowerPointer < m:
    if (
        max(desiredList[upperPointer] - k, 0)
        <= size[lowerPointer]
        <= desiredList[upperPointer] + k
    ):
        count += 1
        lowerPointer += 1
    elif size[lowerPointer] < max(desiredList[upperPointer] - k, 0):
        lowerPointer += 1
    else:
        upperPointer += 1
print(count)
