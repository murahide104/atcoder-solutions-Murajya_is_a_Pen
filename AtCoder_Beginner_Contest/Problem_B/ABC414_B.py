n = int(input())
s = ""
for i in range(n):
    c, l = input().split()
    l = int(l)
    if 100 < l:
        print("Too Long")
        exit()
    
    s += c * l
    
    if 100 < len(s):
        print("Too Long")
        exit()

print(s)