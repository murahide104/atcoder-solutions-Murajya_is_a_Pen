n, m = map(int, input().split())
c_li = list(input().split())
d_li = list(input().split())
p_li = list(map(int, input().split()))
price = 0

for i in range(n):
    if c_li[i] not in d_li:
        price += p_li[0]
    else:
        price += p_li[d_li.index(c_li[i]) + 1]
else:
    print(price)