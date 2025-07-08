n, k = map(int, input().split())

count = 1
for i in range(n):
    if i == 0:
        count *= k
    else:
        count *= k-1

print(count)


# print(k * (k-1)**(n-1))