x = int(input())
a = int(input())
b = int(input())

x -= a
print(x - (x // b) * b)