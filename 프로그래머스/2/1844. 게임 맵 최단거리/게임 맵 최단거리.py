def solution(maps):
    from collections import deque
    
    n, m = len(maps), len(maps[0])
    
    DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    def is_valid(i, j):
        return 0 <= i < n and 0 <= j < m
    
    
    visited = [[-1] * m for _ in range(n)]
    
    q = deque([(0, 0)])
    visited[0][0] = 1
    
    while q:
        i, j = q.popleft()
        
        for di, dj in DIRS:
            
            ni, nj = i + di, j + dj
            
            if not is_valid(ni, nj):
                continue

            if maps[ni][nj] == 0: # 벽이면 못감
                continue
            
            if visited[ni][nj] > 0: # 방문했으면 못감
                continue
                        
            visited[ni][nj] = visited[i][j] + 1 # 방문표시 + 거리누적
            q.append((ni, nj)) # q에 추가해서 다음 위치 넣기
    

    return visited[n - 1][m - 1]