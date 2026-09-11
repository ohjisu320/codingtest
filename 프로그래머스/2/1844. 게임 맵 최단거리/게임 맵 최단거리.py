


def solution(maps):
    from collections import deque
    
    DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def is_valid(i, j):
        return 0 <= i < N and 0 <= j < M
    
    N = len(maps)
    M = len(maps[0])
    
    print(N, M)
    
    
    q = deque([(0, 0)])
    
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1
    
    while q:
        i, j = q.popleft()
        
        for di, dj in DIRS:
            ni, nj = i + di, j + dj

            if not is_valid(ni, nj):
                continue
            if visited[ni][nj] != -1:
                continue
            if maps[ni][nj] == 0:
                continue

            visited[ni][nj] = visited[i][j] + 1 # 1 증가
            q.append((ni, nj))
            

            
    return visited[N - 1][M - 1]