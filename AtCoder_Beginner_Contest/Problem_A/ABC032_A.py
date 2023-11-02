a = int(input())
b = int(input())
n = int(input())
ans = n

while True:
    if ans % a == 0 and ans % b == 0:
        print(ans)
        break
    ans += 1