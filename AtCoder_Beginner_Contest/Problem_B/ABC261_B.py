n = int(input())
result = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if result[i][j] == "W" and result[j][i] != "L":
            exit(print("incorrect"))
        elif result[i][j] == "L" and result[j][i] != "W":
            exit(print("incorrect"))
else:
    print("correct")