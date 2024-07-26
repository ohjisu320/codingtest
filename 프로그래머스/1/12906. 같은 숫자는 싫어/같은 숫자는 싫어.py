def solution(arr):
    answer = []
    for x in range(len(arr)) : 
        if x==0 or arr[x] != arr[x-1] :
            answer.append(arr[x])
        else :
            pass
    return answer