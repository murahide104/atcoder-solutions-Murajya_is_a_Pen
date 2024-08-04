n = input()

if len(n) <= 2:
  print(100-int(n))
else:
  print(100-int(n[1:]))