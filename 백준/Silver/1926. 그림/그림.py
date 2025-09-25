from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()



DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(start_i, start_j) :
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1
    dist = 1

    while q :
        i, j = q.popleft()

        for di, dj in DIRS :
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < m) :
                continue
            if visited[ni][nj]:
                continue
            if not graph[ni][nj] :
                continue
            visited[ni][nj] = 1
            dist += 1
            q.append((ni, nj))
    return dist

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

max_dist = 0
cnt = 0
for i in range(n) :
    for j in range(m):
        if graph[i][j] and not visited[i][j] :
            cnt += 1
            max_dist = max(max_dist, bfs(i, j))

print(cnt)
print(max_dist)
