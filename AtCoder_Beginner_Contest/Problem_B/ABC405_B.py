n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n+1):
    for j in range(1, m+1):
        if j not in a:
            print(cnt)
            exit()
    
    a.pop()
    cnt += 1

print(cnt)