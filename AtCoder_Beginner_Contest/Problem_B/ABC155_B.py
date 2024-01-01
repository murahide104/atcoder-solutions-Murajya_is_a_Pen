n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    if l[i] % 2 == 0:
        if l[i] % 3 == 0 or l[i] % 5 == 0:
            continue
        else:
            exit(print("DENIED"))
else:
    print("APPROVED")