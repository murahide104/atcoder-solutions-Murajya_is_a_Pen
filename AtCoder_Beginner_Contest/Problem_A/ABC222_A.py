n = input()
if len(n) == 4:
    print(n)
elif len(n) == 3:
    print("0"+n)
elif len(n) == 2:
    print("00"+n)
else:
    print("000"+n)