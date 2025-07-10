s = input()
t = input()

for i in range(2, len(s)):
    if s[i].isupper() and s[i-1] not in t:
        print("No")
        exit()

print("Yes")