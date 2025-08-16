s = input()

ans = 0

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        t = s[i:j]

        if t[0] == "t" and t[-1] == "t" and len(t) >= 3:
            x = t.count("t")
            late = (x - 2) / (len(t) - 2)
            ans = max(ans, late)

print(ans)