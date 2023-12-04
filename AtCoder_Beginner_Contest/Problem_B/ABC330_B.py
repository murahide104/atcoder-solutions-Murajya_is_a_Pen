n, l, r = map(int, input().split())
a = list(map(int, input().split()))

result =[]
for i in range(n):
    if l <= a[i] <= r:
        result.append(a[i])
    elif a[i] <= l:
        result.append(l)
    else:
        result.append(r)

print(*result)