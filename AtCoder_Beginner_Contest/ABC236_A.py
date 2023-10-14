s = list(input())
a, b = map(int, input().split())

x = s[a-1]
s[a-1] = s[b-1]
s[b-1] = x
print(*s, sep="")