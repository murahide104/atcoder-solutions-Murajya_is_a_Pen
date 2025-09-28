n = int(input())
a = list(map(int, input().split()))

check = []
p = [0] * n

for i in range(n):
    if a[i] > 0:
        if a[i] in check:
            print("No")
            exit()

        check.append(a[i])
        p[i] = a[i]

for i in range(n):
    if p[i] == 0:
        for j in range(1, n+1):
            if j not in check:
                p[i] = j
                check.append(j)
                break

if 0 not in p:
    print("Yes")
    print(*p)
else:
    print("No")