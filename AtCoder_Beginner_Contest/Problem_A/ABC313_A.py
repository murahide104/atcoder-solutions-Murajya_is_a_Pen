n = int(input())
l = list(map(int, input().split()))

if len(l) == 1:
    exit(print(0))
    
p1 = l.pop(0)
max_l = max(l)

if p1 <= max_l:
    print(max_l - p1 + 1)
else:
    print(0)