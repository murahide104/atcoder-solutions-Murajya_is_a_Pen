n, m = map(int, input().split())
li = list(map(int, input().split()))

if sum(li) <= m:
    print("Yes")
else:
    print("No")