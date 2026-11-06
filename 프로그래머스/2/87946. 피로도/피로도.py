def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)
    
    def dfs(now_k, possible):
        nonlocal answer
        
        answer = max(answer, possible)
        
        for i in range(len(dungeons)):
            need, use = dungeons[i]
            
            if not visited[i] and now_k >= need:
                visited[i] = 1
                dfs(now_k - use, possible + 1)
                visited[i] = 0
    dfs(k, 0)
    return answer


