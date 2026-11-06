from collections import Counter, defaultdict

def solution(points, routes):
    
    visited = defaultdict(Counter)
    answer = 0
    
    for route in routes:
        sp = route[0]
        r, c = points[sp - 1]
        time = 0
        
        visited[time][(r, c)] += 1
        
        for np in route[1:]:
            nr, nc = points[np - 1]
            
            while r != nr:
                r += 1 if r < nr else -1
                time += 1
                visited[time][(r, c)] += 1
            while c != nc:
                c += 1 if c < nc else -1
                time += 1
                visited[time][(r, c)] += 1

    for v_points in visited.values():
        for v_point in v_points.values():
            if v_point > 1:
                answer += 1
                    
                
    return answer