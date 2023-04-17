import math
a = int(input())
b = int(input())

if a < b:
  print(b-a)
elif a > b:
  x = a//b
  print(b*(x+1)-a)
else:
  print(0)