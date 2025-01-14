def solution(n, k):
    free = n/10
    if free >= 1 :
        k = k-int(free)
        if k <0 :
            k=0
    answer = 12000*n+2000*k
        
    
        
    return answer