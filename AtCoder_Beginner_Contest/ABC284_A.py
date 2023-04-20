n = int(input())
L = [input() for _ in range(n)]
for i in range(len(L), 0, -1):
    print(L[i-1])