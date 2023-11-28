s = input()
t = input()

for i in range(len(t)):
    if t[0:i+1] == s:
        exit(print("Yes"))
else:
    print("No")