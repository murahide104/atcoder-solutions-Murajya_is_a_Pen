n = int(input())
l = list(map(int, input().split()))
sort_l = sorted(l)

print(l.index(sort_l[-2]) + 1)