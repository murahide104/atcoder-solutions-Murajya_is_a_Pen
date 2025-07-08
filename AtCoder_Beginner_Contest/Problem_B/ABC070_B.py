a, b, c, d = map(int, input().split())

if c < b and a < d:
    print(min(b, d) - max(a, c))
else:
    print(0)
    
# overlap = max(0, min(b, d) - max(a, c))
# print(overlap)
