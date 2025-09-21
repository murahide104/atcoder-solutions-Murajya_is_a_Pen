from collections import deque

n = int(input())
skill = [(0, 0)]

for _ in range(n):
    skill.append(tuple(input().split()))



get = [False] * (n+1)

queue = deque()
queue.append(0)

while queue:
    skill_n = queue.popleft()
    
    for i in range(1, len(skill)):
        r, l = skill[i]
        

        # 進めるかチェック
        if skill[l] and not skill[r]:
            get[r] = True
            queue.append(r)
        elif not skill[l] and skill[r]:
            get[l] = True
            queue.append(l)
        elif l == 0 and r == 0:
            get[i] = True
            queue.append((i))

skill.count(True)