n, t, p = map(int, input().split())
l = list(map(int, input().split()))
t_distance = []

for i in l:
  if t <= i:
    t_distance.append(0)
  else:
    t_distance.append(t-i)

t_distance.sort()

print(t_distance[p-1])