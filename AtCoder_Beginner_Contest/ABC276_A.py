s = input()
a_idx = None

for i in range(len(s)):
    if s[i] == "a":
        a_idx = i+1
else:
    if a_idx == None:
        print(-1)
    else:
        print(a_idx)