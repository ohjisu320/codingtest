
from collections import deque
import sys
input  = lambda :sys.stdin.readline().rstrip()

DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def is_valid(i, j):
    return 0 <= i < M and 0 <= j < N

N, M = map(int, input().split())

graph = [list(input()) for _ in range(M)] # 가로 N 세로 M

def bfs(si, sj, team):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    cnt = 1

    while q:
        i, j = q.popleft()

        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if not is_valid(ni, nj):
                continue
            if visited[ni][nj]:
                continue
            if graph[ni][nj] != team:
               continue
            visited[ni][nj] = 1
            cnt += 1
            q.append((ni, nj))
    return cnt

w_result = b_result = 0
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j]: continue
        team = graph[i][j]
        cnt = bfs(i, j, team)
        if team == 'W':
            w_result += cnt ** 2
        else:
            b_result += cnt ** 2

print(w_result, b_result)