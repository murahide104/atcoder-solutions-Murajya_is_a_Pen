n, q = map(int, input().split())
x_li = list(map(int, input().split()))

b_cnt = [0]*n
b_i = []

for x in x_li:
    if 0 < x:
        b_cnt[x-1] += 1
        b_i.append(x)
    else:
        min_i = b_cnt.index(min(b_cnt))
        b_cnt[min_i] += 1
        b_i.append(min_i+1)

print(*b_i)