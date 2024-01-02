n, m = map(int, input().split())
l = list(map(int, input().split()))

check = sum(l)/(4*m)
count = 0

for i in range(n):
    if check <= l[i]:
        count += 1

print("Yes" if m <= count else "No")