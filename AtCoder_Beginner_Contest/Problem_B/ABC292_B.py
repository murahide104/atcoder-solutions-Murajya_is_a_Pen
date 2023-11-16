n, q = map(int, input().split())
di = {}

for i in range(1, n+1):
    di[i] = 0
    
for i in range(q):
    e, x = map(int, input().split())
    
    if e == 1:
        di[x] += 1
    elif e == 2:
        di[x] += 2
    elif e == 3:
        if di[x] >= 2:
            print("Yes")
        else:
            print("No")