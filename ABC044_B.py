t = input()
for i in range(len(t)):
  if t.count(t[i]) % 2 != 0:
    print("No");break
else:
  print("Yes")