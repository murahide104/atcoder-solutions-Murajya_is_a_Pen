s = input()
t = ""

last_o_idx = None
first = True
for i in range(len(s)):
    if s[i] == "#":
        t = t + "#"
        continue
    
    if s[i] == "." and first:
        t = t + "o"
        last_o_idx = i
        first = False
        continue
    
    for j in range(last_o_idx, i): # 一番近い左のoから今いる位置まで
        if s[j] == "#":
            t = t + "o"
            last_o_idx = i
            break
    else:
        t = t + "."
            

print(t)
