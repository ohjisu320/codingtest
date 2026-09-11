
def solution(progresses, speeds):
    import math
    answer = []
    
    last_days = []
    cnt = 1
    for i in range(len(progresses)):
        last_days.append( math.ceil( (100 - progresses[i])/speeds[i]))
    
    comp = last_days[0]
    for i in range(1, len(last_days)):
        if comp >= last_days[i]:
           cnt += 1
        else: 
            answer.append(cnt)
            cnt = 1
            comp = last_days[i]
        if i == len(last_days) -1:
            answer.append(cnt)
        

    return answer