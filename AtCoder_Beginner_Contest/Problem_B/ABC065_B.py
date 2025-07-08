n = int(input())
button = [int(input()) for _ in range(n)]

move_i = 0

visited = set()

for i in range(len(button)):
    if button[move_i] == 2:
        print(i+1)
        exit()

    if button[move_i] in visited:
        print(-1)
        exit()

    visited.add(button[move_i])
    move_i = button[move_i] -1
else:
    print(-1)
