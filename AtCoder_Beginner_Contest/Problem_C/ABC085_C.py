n, y = map(int, input().split())

flag = False

for i in range(n+1):
    if flag: break
    for j in range((n+1)-i):
        k = n - i - j
        if (i*1000) + (j*5000) + (k*10000) == y:
            flag = True
            money = [k, j, i]
            break

if flag:
    print(*money)
else:
    print("-1 -1 -1")