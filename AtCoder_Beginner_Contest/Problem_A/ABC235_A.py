n = input()

abc = int(n[0])*100 + int(n[1])*10 + int(n[2])
bca = int(n[1])*100 + int(n[2])*10 + int(n[0])
cab = int(n[2])*100 + int(n[0])*10 + int(n[1])

print(abc+bca+cab)