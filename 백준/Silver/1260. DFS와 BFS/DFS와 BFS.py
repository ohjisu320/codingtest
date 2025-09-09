from collections import deque
import sys
input = sys.stdin.readline

def dfs(start) :
    visited = []
    arr = [start]
    while arr :
        S = arr.pop()
        if S in visited : continue
        visited.append(S)
        print(S, end=' ')
        for e in sorted(adj[S], reverse=True) :
            arr.append(e)
    return visited
            

def bfs(start) :
    visited = []
    q = deque([start])
    while q :
        S = q.popleft()
        if S in visited : continue
        visited.append(S)
        print(S, end=' ')
        for e in sorted(adj[S]) :
            q.append(e)
    return visited


N, M, V = map(int, input().split())

# 인접 리스트 생성
adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

dfs(V)
print()
bfs(V)