t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    count = 0
    for j in range(n):
        if l[j] % 2 == 1:
            count += 1
        
    print(count)