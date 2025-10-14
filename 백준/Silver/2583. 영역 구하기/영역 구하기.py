import sys
from collections import deque

# 함수 + 초기값 설정
input = sys.stdin.readline
DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(start_i, start_j):
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if not (0 <= ni < M and 0 <= nj < N):
                continue
            if not visited[ni][nj] and graph[ni][nj] == 0:
                visited[ni][nj] = 1  
                cnt += 1  
                q.append((ni, nj))  

    return cnt

# 사용자 입력
M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

visited = [[0] * N for _ in range(M)]
areas = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]: # 방문 가능 체크 + 방문 체크
            areas.append(bfs(i, j))


print(len(areas))
print(*sorted(areas))