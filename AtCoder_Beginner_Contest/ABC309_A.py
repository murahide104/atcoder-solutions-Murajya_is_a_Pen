a, b = map(int, input().split())
if a + 1 == b or a - 1 == b:
    if 1 <= a <= 3 and 1 <= b <= 3:
        print("Yes")
    elif 4 <= a <= 6 and 4 <= b <= 6:
        print("Yes")
    elif 7 <= a <= 9 and 7 <= b <= 9:
        print("Yes")
    else:
        print("No")
else:
    print("No")