a, b = map(int, input().split())

if b // 2 == a or a*2 == b or a*2+1 == b:
  print("Yes")
else:
  print("No")