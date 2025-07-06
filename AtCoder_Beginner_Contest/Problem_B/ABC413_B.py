n = int(input())
li = []
concat_li = []

for i in range(n):
    s = input()
    li.append(s)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if li[i] + li[j] not in concat_li:
            concat_li.append(li[i] + li[j])
        if li[j] + li[i] not in concat_li:
            concat_li.append(li[j] + li[i])

print(len(concat_li))