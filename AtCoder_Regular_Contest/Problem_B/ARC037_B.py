n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False]*(n+1)

def dfs(i):
    global nodes
    global edges
    
    # 引き返し
    if visited[i]:
        return
    
    # 記録
    visited[i] = True
    nodes += 1   #ノードをカウント
    
    # 次のノードに進む
    for value in graph[i]:
        edges += 1   # エッジをカウント
        dfs(value)

    
ans = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    
    nodes = 0
    edges = 0
    dfs(i)

    if edges // 2 == nodes - 1:
        ans += 1

print(ans)