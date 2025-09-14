n, r = map(int, input().split())
L = list(map(int, input().split()))

left = L[:r]
right = L[r:][::-1]

count = {"left":0, "right":0}

flag = 0
for v in left:
    if v == 0 and flag == 0:
        flag = 1
        count["left"] += 1
    elif v == 0:
        count["left"] += 1
    elif v == 1 and flag == 1:
        count["left"] += 2
    else:
        pass

flag = 0
for v in right:
    if v == 0 and flag == 0:
        flag = 1
        count["right"] += 1
    elif v == 0:
        count["right"] += 1
    elif v == 1 and flag == 1:
        count["right"] += 2
    else:
        pass

print(count["left"] + count["right"])