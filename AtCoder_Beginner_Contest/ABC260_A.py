t = input()
for i in range(len(t)):
    if t.count(t[i]) == 1:
        print(t[i])
        break
else:
    print(-1)