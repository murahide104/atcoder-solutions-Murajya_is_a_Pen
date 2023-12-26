n = int(input())
l = [list(input()) for _ in range(n)]
result = []

for i in range(n):
    count = 0
    for j in range(n):
        if l[i][j] == "o":
            count += 1
    result.append(count)

for i in range(n):
    max_n = max(result)
    if max_n == -1:
        break
    
    for j in range(n):
        if result[j] == max_n:
            print(j+1)
            result[j] = -1