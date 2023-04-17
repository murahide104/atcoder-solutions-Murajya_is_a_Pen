n, s, t = map(int, input().split())
w = int(input())
count_day = 0
for i in range(n-1):
    a = int(input())
    w += a
    if s <= w and w <= t:
        count_day += 1
print(count_day)