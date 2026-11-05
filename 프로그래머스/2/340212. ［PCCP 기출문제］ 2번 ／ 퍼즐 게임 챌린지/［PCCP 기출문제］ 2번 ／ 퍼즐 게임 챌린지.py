def solution(diffs, times, limit):
    
    left = 1
    right = max(diffs)
    
    while left < right:
        
        level = (left + right) // 2
        cnt = 0
    
        for i in range(len(diffs)):
            nd, nt = diffs[i], times[i]
            
            if nd <= level: # 난이도보다 숙련도가 같거나 낮으면
                cnt += nt   # cnt에 nt 현재 푼 시간 더하기
            else:           # 난이도가 숙련도보다 높으면
                cnt += (nd - level) * (nt + times[i - 1]) + nt
                       # 틀리는 횟수 * (이전 퍼즐속도 + 현재퍼즐속도) + 현재 퍼즐속도
            if cnt > limit: break
            
        if cnt <= limit:
            right = level
            
        else:
            left = level + 1
        
    return left
    
            
  