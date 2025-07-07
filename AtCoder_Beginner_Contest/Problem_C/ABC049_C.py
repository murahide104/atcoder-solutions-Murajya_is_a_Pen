s = input()[::-1]
text = ["dream", "dreamer", "erase", "eraser"]
reversed_text = [word[::-1] for word in text]

while s:
    for t in reversed_text:
        if s[:len(t)] == t:
            s = s[len(t):]
            break
    else:
        print("NO")
        exit()
else:
    print("YES")