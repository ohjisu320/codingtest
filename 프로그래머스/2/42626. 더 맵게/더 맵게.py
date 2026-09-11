import heapq

def solution(scoville, K):
    answer = 0
    comp = 0
    heapq.heapify(scoville)
    while scoville and scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
        
            heapq.heappush(scoville, first + second * 2)
            answer += 1
        else: return -1
    if scoville[0] < K:
        return -1
    else:            
        return answer


    
       