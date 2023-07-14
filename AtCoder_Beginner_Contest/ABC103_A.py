l = list(map(int, input().split()))
l.sort()
print(abs(l[0]-l[1])+abs(l[1]-l[2]))