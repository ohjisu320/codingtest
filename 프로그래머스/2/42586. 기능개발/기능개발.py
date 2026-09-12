def solution(progresses, speeds):
    import math
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) /speeds[i]))
    
    comp = days[0]
    cnt = 1
    
    for i in range(1, len(days)):
        if comp < days[i]:
            answer.append(cnt)
            cnt = 1
            comp = days[i]
        else:
            cnt += 1
    
    answer.append(cnt)
        
    return answer