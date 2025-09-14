n = int(input())
L = list(map(int, input().split()))

indices = [i for i, v in enumerate(L) if v == 1]

if indices:
    print(max(indices) - min(indices))
else:
    print(0)
