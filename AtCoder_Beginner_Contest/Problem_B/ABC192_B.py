s = input()
flag = False

for i in range(len(s)):
    if i % 2 == 0:
        if not s[i].islower():
            flag = True
    else:
        if s[i].islower():
            flag = True

print("No" if flag else "Yes")