n, a, b = map(int, input().split())

result = 0

for i in range(1, n+1):
    li = list(str(i))
    total = sum(list(map(int, li)))
    if a <= total <= b:
        result += i

print(result)