""" TLE """
# n, m = map(int, input().split())
# s = input()
# t = input()

# for _ in range(m):
#     l, r = map(int, input().split())

#     xxx = s[l-1:r]
#     s = s[:l-1] + t[l-1:r] + s[r:]
#     t = t[:l-1] + xxx + t[r:]

# print(s)


""" TrueFalseでやってみる (TLE) """
# n, m = map(int, input().split())
# s = list(input())
# t = list(input())

# check = [False] * n

# for _ in range(m):
#     l, r = map(int, input().split())
#     check[l-1:r] = [not x for x in check[l-1:r]]

# for i in range(n):
#     if check[i]:
#         print(t[i], end="")
#     else:
#         print(s[i], end="")
# print()


""" 一度で求める """
n, m = map(int, input().split())
s = list(input())
t = list(input())

check = [False] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    
    if check[l-1]:
        check[l-1] = False
    else:
        check[l-1] = True
    
    if check[r]:
        check[r] = False
    else:
        check[r] = True 

ans = []

flag = False
for i in range(n):
    if check[i] == True:
        flag = not flag
    
    if flag:
        ans.append(t[i])
    else:
        ans.append(s[i])


print("".join(ans))