from collections import deque
T = int(input())

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]



def bfs(i, j) : # bfs - 간잽이
    q = deque([(i, j)])
    visited[i][j] = 1
    while q :
        i, j =  q.popleft()
        for di, dj in dir :
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj  < M and graph[ni][nj] == 1 and visited[ni][nj] == 0 :
                q.append((ni, nj))
                visited[ni][nj] = 1



def dfs(i, j) : # dfs - 한놈만 패는 애
    q = deque([(i, j)])
    visited[i][j] = 1
    while q :
        i, j =  q.pop()
        for di, dj in dir :
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj  < M and graph[ni][nj] == 1 and visited[ni][nj] == 0 :
                q.append((ni, nj))
                visited[ni][nj] = 1



for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*M for _ in range(N)]

    for _ in range(K) :
        i, j = map(int, input().split())
        graph[j][i] = 1
    cnt = 0

    visited = [[0]*M for _ in range(N)]

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1 and visited[i][j] == 0 :
                cnt += 1
                bfs(i, j)
    print(cnt)