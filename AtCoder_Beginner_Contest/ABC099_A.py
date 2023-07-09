n = int(input())
if n < 1000:
    if n < 10:
        print("ABC00"+str(n))
    elif n < 100:
        print("ABC0"+str(n))
    else:
        print("ABC"+str(n))
else:
    if n-999 < 10:
        print("ABD00"+str(n-999))
    elif n-999 < 100:
        print("ABD0"+str(n-999))
    else:
        print("ABD"+str(n-999))