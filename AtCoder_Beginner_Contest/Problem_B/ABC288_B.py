n, k = map(int, input().split())
l = []

for i in range(n):
    l.append(input())

l = l[:k]
l.sort()

for i in range(k):
    print(l[i])