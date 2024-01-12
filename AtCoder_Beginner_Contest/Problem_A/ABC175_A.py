s = input()
count = 0
max_count = 0
for i in range(3):
    if s[i] == "R":
        count += 1
        if max_count < count:
            max_count = count
    else:
        if max_count < count:
            max_count = count
        count = 0

print(max_count)