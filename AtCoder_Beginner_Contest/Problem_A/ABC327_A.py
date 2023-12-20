n = int(input())
s = input()

for i in range(1, n):
    if s[i] == "a":
        if s[i-1] == "b":
            exit(print("Yes"))
    if s[i] == "b":
        if s[i-1] == "a":
            exit(print("Yes"))
else:
    print("No")