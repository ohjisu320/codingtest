def solution(array, height):
    answer = 0
    for i in sorted(array, reverse=True) :
        if i > height :
            answer+=1
        else :
            break
    return answer
