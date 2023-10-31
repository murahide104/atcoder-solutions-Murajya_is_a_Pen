l = list(map(int, input().split()))

for i in range(7):
    if not (l[i] <= l[i+1]):
        break
    elif not (100 <= l[i] <= 675):
        break
    elif not (l[i] % 25 == 0):
        break
    if i == 6:
        i += 1
        if not (100 <= l[i] <= 675):
            break
        elif not (l[i] % 25 == 0):
            break
else:
    exit(print("Yes"))
    
print("No")