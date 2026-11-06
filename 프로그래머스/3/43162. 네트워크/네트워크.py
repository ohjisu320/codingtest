def solution(n, computers):
    visited = [0] * n
    
    answer = 0
    
    def dfs(x):
        visited[x] = True
        
        for next_node in range(n):
            if not computers[x][next_node]:
                continue
            if visited[next_node]:
                continue
            
            dfs(next_node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer