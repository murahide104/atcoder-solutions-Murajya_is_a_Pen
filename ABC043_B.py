t = input()
result = []
for i in range(len(t)):
  if t[i] == "B":
    if len(result) == 0:
        pass
    else:
        result.pop(-1)
  else:
    result.append(t[i])
print(*result, sep="")