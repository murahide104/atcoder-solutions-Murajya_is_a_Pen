n = int(input())
l = list(map(int, input().split()))
n = len(l)
l.sort()

if n < 3: print(0); exit()

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if l[i] == l[j]: continue
        for k in range(j+1,n):
            if l[j] == l[k]: continue
            if l[k] < l[i] + l[j]:
                cnt += 1
            else:
                break

print(cnt)