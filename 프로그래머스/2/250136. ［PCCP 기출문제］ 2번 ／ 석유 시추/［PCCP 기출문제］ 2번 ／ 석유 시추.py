from collections import deque

DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def solution(land):
    N = len(land)
    M = len(land[0])
    visited = [[0] * M for _ in range(N)]
    check = [0] * M

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if not land[i][j]:
                continue
            cnt, min_j, max_j = bfs(i, j, N, M, visited, land)

            for c in range(min_j, max_j + 1):
                check[c] += cnt

    return max(check)


def is_valid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M


def bfs(i, j, N, M, visited, land):
    q = deque([(i, j)])
    visited[i][j] = 1

    min_j = j
    max_j = j

    cnt = 1

    while q:
        si, sj = q.popleft()

        for di, dj in DIRS:
            ni, nj = si + di, sj + dj
            if not is_valid(ni, nj, N, M):
                continue
            if land[ni][nj] == 0:
                continue
            if visited[ni][nj]:
                continue
            min_j = min(min_j, nj)
            max_j = max(max_j, nj)
            cnt += 1

            q.append((ni, nj))
            visited[ni][nj] = 1

    return cnt, min_j, max_j