n = int(input())
s = input()
l = []

for i in range(n):
    for j in range(2):
        l.append(s[i])

print(*l, sep= "")