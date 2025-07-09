abcd = list(map(int, input()))
op = []


for i in range(1 << 3):
    bit = format(i, '03b')
    op = str(bit).replace("1", "+").replace("0", "-")
    
    total = abcd[0]
    for j in range(3):
        if op[j] == "+":
            total += abcd[j+1]
        else:
            total -= abcd[j+1]
    else:
        if total == 7:
            print(abcd[0], end="")
            for k in range(3):
                print(op[k]+ str(abcd[k+1]), end="")
            print("=7")
            exit()
