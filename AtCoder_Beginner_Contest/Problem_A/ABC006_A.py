n = input()
for i in range(len(n)):
  if n[i] == "3":
    print("YES");break
  elif int(n)%3 == 0:
    print("YES");break
else:
    print("NO")