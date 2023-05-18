r, c = map(int, input().split())
l = list(input().split() for _ in range(2))

print(l[r-1][c-1])