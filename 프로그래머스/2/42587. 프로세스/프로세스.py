from collections import deque

def solution(priorities, location):
    
    q = deque((p, l) for l, p in enumerate(priorities))
    
    cnt = 0
    while q:
        flag = False
        now_p, now_l = q.popleft()
        
        for next_p, next_l in q:
            if now_p < next_p: # 우선순위가 더 큰게 존재함
                flag = True
                break
        
        if flag:
            q.append((now_p, now_l))
        else:
            cnt += 1 # 실행한 횟수
            if now_l == location:
                return cnt
    return
        
    