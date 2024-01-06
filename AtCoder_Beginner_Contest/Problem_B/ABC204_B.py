n = int(input())
a = list(map(int, input().split()))
total = 0

for i in range(n):
    if 10 <= a[i]:
        total += a[i] - 10

print(total)