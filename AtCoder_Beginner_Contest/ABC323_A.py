s = input()
for i in range(1, len(s), 2):
    if s[i] == "1":
        exit(print("No"))
else:
    print("Yes")