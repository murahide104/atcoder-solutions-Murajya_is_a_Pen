t = input()
cnt = 0
for i in range(len(t)):
    if t[i] == "v":
        cnt += 1
    else:
        cnt += 2
print(cnt)