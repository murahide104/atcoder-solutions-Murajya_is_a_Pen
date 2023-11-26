n, x = map(int, input().split())
l = list(map(int, input().split()))

total = 0

for i in range(n):
    if l[i] <= x:
        total += l[i]

print(total)