n = int(input())
s = input()
t = input()

if s == t:
    print("Yes")
else:
    for i in range(n):
        if s[i] == t[i]:
            pass
        elif (s[i] == "o" or s[i] == "0") and (t[i] == "o" or t[i] == "0"):
            pass
        elif (s[i] == "l" or s[i] == "1") and (t[i] == "l" or t[i] == "1"):
            pass
        else:
            print("No")
            break
    else:
        print("Yes")