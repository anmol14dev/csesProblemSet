n, m, k = [int(x) for x in input().split()]
desiredList = [(max(int(x) - k, 0), int(x) + k) for x in input().split()]
