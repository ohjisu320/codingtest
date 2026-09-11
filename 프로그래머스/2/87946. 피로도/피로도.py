def solution(k, dungeons):
    #재귀?dfs?
    def dfs(cnt, now_k):
        
        nonlocal answer
        answer = max(answer, cnt) # 지금까지 저장한 answer와 현재 방문 횟수 중 큰것
        
        
        for i in range(len(dungeons)): # 던전 하나씩 들르기
            
            if visited[i]:
                continue
                
            if now_k >= dungeons[i][0]: # 지금 체력이 던전 필요 체력보다 높으면
                visited[i] = 1
                dfs(cnt + 1, now_k - dungeons[i][1]) # 갈 수 있다
                visited[i] = 0
                
            
    
    
    answer = -1
    visited = [0] * len(dungeons)
    dfs(0, k) # 던전 방문 횟수, 현재 피로도
        
    return answer