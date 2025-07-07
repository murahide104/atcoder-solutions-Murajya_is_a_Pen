n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice = 0
bob = 0

while len(a) > 0:
    alice += a.pop(0)

    if len(a) == 0:
        break
    
    bob += a.pop(0)

print(alice - bob)
