n, x = map(int, input().split())
s = input()

for i in s:
    if i == "o":
        x += 1
    else:
        if 1 <= x:
            x -= 1

print(x)