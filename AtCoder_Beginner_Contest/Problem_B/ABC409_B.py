n = int(input())
A = list(map(int, input().split()))

for x in range(n, -1, -1):
    cnt = 0
    for a in A:
        if x <= a:
            cnt += 1
    
    if x <= cnt:
        print(x)
        exit()