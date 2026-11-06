from collections import deque

DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def is_valid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M 


def solution(maps):
    
    N = len(maps)       # 행
    M = len(maps[0])    # 열
    
    visited = [[-1] * M for _ in range(N)]

    q = deque([(0, 0)])
    visited[0][0] = 1

    
    while q:
        si, sj = q.popleft()
        
        for di, dj in DIRS:
            ni, nj = si + di, sj + dj
            
            if not is_valid(ni, nj, N, M):
                continue
                
            if visited[ni][nj] > 0 :
                continue
                
            if not maps[ni][nj]:
                continue

            visited[ni][nj] = visited[si][sj] + 1 # 거리 누적
            q.append((ni, nj)) # q에 넣기

    return visited[N - 1][M - 1]
