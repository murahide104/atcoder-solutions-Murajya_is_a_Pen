n = int(input())
a_list = list(map(int, input().split()))
count = 0
for i in range(n):
    if a_list[i-count] % 2 == 1:
        del a_list[i-count]
        count += 1
print(*a_list, sep=" ")