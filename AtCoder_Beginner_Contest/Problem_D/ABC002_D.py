from itertools import combinations

n, m = map(int, input().split())   # n=議員数 m=関係数
xy = set(tuple(map(int, input().split())) for _ in range(m))

ans = 1

for i in range(1 << n):
    invalid = False
    
    member = []
    for j in range(n):
        if (i >> j) & 1:
            member.append(j+1)
    
    for x, y in combinations(member, 2):
        if (x, y) not in xy:
            invalid = True
            break
    
    if invalid: continue
    
    ans = max(ans, len(member))

print(ans)  
