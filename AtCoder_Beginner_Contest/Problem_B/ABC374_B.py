s = input()
t = input()

answer = 0
if len(s) == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            answer = i + 1
            break
else:
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            answer = i + 1
            break
    else:
        answer = i + 2

print(answer)