import copy

def rotate_90(grid):
    n = len(grid)
    return [[grid[(n-1)-j][i] for j in range(n)] for i in range(n)]

n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

check = []

for i in range(4):
    check_s = copy.deepcopy(s)
    for _ in range(i):
        check_s = rotate_90(check_s)
    
    cnt = 0
    for j in range(n):
        for k in range(n):
            if check_s[j][k] != t[j][k]:
                cnt += 1
    
    check.append(i+cnt)

print(min(check))