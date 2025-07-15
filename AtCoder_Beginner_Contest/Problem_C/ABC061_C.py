s = input()

if len(s) == 1:
    print(s)
    exit()

total = 0

for i in range(1 << len(s)-1):
    bit = format(i, f"0{len(s)-1}b")
    num = s[0]
    
    for j in range(len(s)-1):
        if bit[j] == "0":
            num +=  s[j+1]
        elif bit[j] == "1":
            total += int(num)
            num = s[j+1]

    total += int(num)

print(total)