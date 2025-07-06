n = int(input())
s = input()

count = 0
if n < 3:
    print(count)
else:
    for i in range(n-2):
        if s[i]=="#" and s[i+1]=="." and s[i+2]=="#":
            count += 1
    else:
        print(count)