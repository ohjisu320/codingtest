from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1) :
    p, c = map(int, input().split()) 
    graph[p].append(c)
    graph[c].append(p)

# 부모/자식 배열
parent = [0] * (N+1)
child = [[] for _ in range(N+1)]

# BFS 
q = deque([1])
visited = [0] * (N+1) 
visited[1] = 1
while q :
    cur = q.popleft()
    for next in graph[cur] :
        if not visited[next] :
            parent[next] = cur
            child[cur].append(next)
            visited[next] = 1
            q.append(next)

for i in range(2, N+1):
    print(parent[i])
