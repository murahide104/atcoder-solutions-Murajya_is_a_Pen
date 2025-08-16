n = int(input())

y = []
x = []

for _ in range(n):
    i, j = map(int, input().split())
    y.append(i)
    x.append(j)

yd = max(y) - min(y)
xd = max(x) - min(x)
md = max(yd, xd)

if md % 2 == 1:
    print(md // 2 + 1)
else:
    print(md//2)