n, k = map(int, input().split())
A = list(map(int, input().split()))

result = 1

for a in A:
    if len(str(result * a)) > k:
        result = 1
    else:
        result *= a

print(result)