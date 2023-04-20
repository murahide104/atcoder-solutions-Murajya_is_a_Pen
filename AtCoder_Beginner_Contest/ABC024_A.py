a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
total = a * s + b * t
if s + t >= k:
    total -= c*(s+t)
print(total)