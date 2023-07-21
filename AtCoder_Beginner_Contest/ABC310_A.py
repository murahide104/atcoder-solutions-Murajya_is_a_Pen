n, p, q = map(int, input().split())
l = list(map(int, input().split()))
n = q + min(l)
if p > n:
    print(p)
else:
    print(n)