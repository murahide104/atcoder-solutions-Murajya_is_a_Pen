n = int(input())
s_li = list(map(int, input().split()))
a_li = [s_li[0]]

for i in range(n-1):
    a_li.append(s_li[i+1] - s_li[i])

print(*a_li)