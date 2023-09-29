s = sorted(list(input()))
set_s = set(s)
if len(set_s) == 2:
    if s.count(s[0]) == s.count(s[3]):
        print("Yes")
    else:
        print("No")
else:
    print("No")