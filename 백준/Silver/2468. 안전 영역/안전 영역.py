import sys
input = lambda :sys.stdin.readline().rstrip()
from collections import deque

DIRS = [[0,1],[1,0],[0,-1],[-1,0]]

def is_valid(i, j):
    return 0 <= i < N and  0 <= j < N

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for i in range(N):
    for j in range(N):
        max_height = max(max_height, graph[i][j])

cnt = 0
for height in range(max_height + 1):
    visited = [[0] * N for _ in range(N)]
    local_cnt = 0

    for i in range(N):
        for j in range(N):

            if graph[i][j] >= height and visited[i][j] == 0:
                local_cnt += 1

                q = deque([(i, j)])
                while q:
                    si, sj = q.popleft()
                    for di, dj in DIRS:
                        ni, nj = si + di, sj + dj
                        if not is_valid(ni, nj):
                            continue
                        if visited[ni][nj]:
                            continue
                        if graph[ni][nj] < height:
                            continue
                        visited[ni][nj] = 1
                        q.append((ni, nj))
                pass
    cnt = max(cnt, local_cnt)



print(cnt)
