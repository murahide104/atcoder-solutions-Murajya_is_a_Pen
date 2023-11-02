n = int(input())
s = input()

for i in range(n):
    if s[i] == "|":
     for j in range(i+1,n):
        if s[j] == "|":
           print("out")
           exit(0)
        if s[j] == "*":
           print("in")
           exit(0)