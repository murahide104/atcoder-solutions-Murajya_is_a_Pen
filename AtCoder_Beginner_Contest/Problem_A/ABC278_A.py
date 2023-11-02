n, k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(k):
    l.pop(0)
    l.append(0)
print(*l)