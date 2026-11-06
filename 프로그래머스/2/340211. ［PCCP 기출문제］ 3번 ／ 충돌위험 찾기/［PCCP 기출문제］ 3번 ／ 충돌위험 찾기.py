from collections import defaultdict, Counter

def solution(points, routes):
    visited = defaultdict(Counter)
    cnt = 0
    
    for route in routes:
        time = 0
        
        r, c = points[route[0] - 1] # 지금 움직일 시작 포인트
        visited[time][(r ,c)] += 1
        
        for point in route[1:]:
            nr, nc = points[point - 1]
            
            while r != nr:
                r += 1 if r < nr else -1
                time += 1
                visited[time][(r, c)] += 1
            while c != nc:
                c += 1 if c < nc else -1
                time += 1
                visited[time][(r, c)] += 1
            
        
    for v in visited.values():
        for vv in v.values():
            if vv > 1:
                cnt += 1
        

    return cnt