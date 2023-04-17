n, l = map(int, input().split())
L = []
for i in range(n):
  x = input()
  L.append(x)
L.sort()
print(*L, sep="")