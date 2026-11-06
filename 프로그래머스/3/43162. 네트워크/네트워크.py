def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    def dfs(x):
        visited[x] = 1
        
        for next_node in range(n):
            if visited[next_node]:
                continue
            if computers[x][next_node] == 0:
                continue
            dfs(next_node)
    
    for i in range(n):
        if visited[i]:
            continue
        dfs(i)
        answer += 1
        
    return answer