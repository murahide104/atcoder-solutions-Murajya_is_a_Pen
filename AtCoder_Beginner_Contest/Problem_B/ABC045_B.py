a = list(input())
b = list(input())
c = list(input())

check = "a"
while True:
    if check == "a":
        if not a:
            print("A")
            break
        else:
            check = a.pop(0)
    elif check == "b":
        if not b:
            print("B")
            break
        else:
            check = b.pop(0)
    else:
        if not c:
            print("C")
            break
        else:
            check = c.pop(0)