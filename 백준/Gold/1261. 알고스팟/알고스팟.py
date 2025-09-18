import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dijkstra(i, j):
    global min_break

    q = deque([(i, j)])
    dists[i][j] = 0

    while q:
        now_i, now_j = q.popleft()

        for di, dj in dirs:
            new_i, new_j = now_i + di, now_j + dj
            if not (0 <= new_i < M and 0 <= new_j < N):
                continue
            if maze[new_i][new_j] == '0': # '0' 만나면 새치기 우선순위에 넣음
                new_dist = dists[now_i][now_j]
                if new_dist < dists[new_i][new_j]:
                    dists[new_i][new_j] = new_dist
                    q.appendleft((new_i, new_j))

            else:
                new_dist = dists[now_i][now_j] + 1 # '1'이면 넣긴 하지만 append로 넣음
                if new_dist < dists[new_i][new_j]:
                    dists[new_i][new_j] = new_dist
                    q.append((new_i, new_j))

    return dists[M - 1][N - 1]

N, M = map(int, input().split()) # N, M이 반대로 들어옴
maze = [list(input()) for _ in range(M)]

min_break = 0
INF = float('inf')
dists = [[INF] * N for _ in range(M)]
cnt = 0
result = dijkstra(0, 0)
print(result)