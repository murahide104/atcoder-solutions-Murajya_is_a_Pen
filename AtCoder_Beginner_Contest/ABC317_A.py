n, h, x = map(int, input().split())
l  = list(map(int, input().split()))
new_l = []
for i in range(n):
    if (x-h) <= l[i]:
        new_l.append(l[i])

print(l.index(min(new_l)) + 1)