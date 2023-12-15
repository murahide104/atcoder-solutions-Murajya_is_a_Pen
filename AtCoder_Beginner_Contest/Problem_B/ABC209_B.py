n, x = map(int, input().split())
l = list(map(int, input().split()))

l = [e if i % 2  == 0 else e-1 for i, e in enumerate(l) ]

print("Yes" if sum(l) <= x else "No")