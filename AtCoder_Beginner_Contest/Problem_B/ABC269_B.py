l = [list(input()) for _ in range(10)]

ac_flag = False
total = 0

for i in range(10):
    for j in range(10):
        if not ac_flag: 
            if l[i][j] == "#": 
                a = i + 1
                b = i + 1
                c = j + 1
                d = c + l[i].count("#") - 1
                ac_flag = True
                break
        else:
            if l[i][j] == "#": 
                b += 1
                break


print(a, b)
print(c, d)