n = int(input())
d = list(map(int, input().split()))

for i in range(n-1):
    total = d[i]
    print(total, end=" ")
    
    for j in range(i+1, n-1):
        total += d[j]
        print(total, end=" ")
        
    print(end="\n")