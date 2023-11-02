n = int(input())
name = [""]*n
age = [""]*n

for i in range(n):
    name[i], age[i] = input().split()

age = list(map(int, age))
min_idx = age.index(min(age))

if min_idx == 0:
    for i in range(n):
        print(name[i])
else:
    idx = min_idx
    while idx < n:
        print(name[idx])
        idx += 1

    for i in range(min_idx):
        print(name[i])