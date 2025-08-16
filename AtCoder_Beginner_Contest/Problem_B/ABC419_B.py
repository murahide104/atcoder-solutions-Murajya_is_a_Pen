q = int(input())

box = []
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        box.append(query[1])
        box.sort()
    else:
        print(box.pop(0))
