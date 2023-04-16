n = int(input())
value = []
while True:
    if n % 2 == 1:
        value.append(1)
        n -= 1
    n = n // 2
    for i in range(n):
        value.append(2)
    break

print(len(value))
for i in value:
    print(i)