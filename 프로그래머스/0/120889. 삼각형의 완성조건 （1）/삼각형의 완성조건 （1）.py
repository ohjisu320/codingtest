def solution(sides):
    if sorted(sides)[-1] < sorted(sides)[0]+sorted(sides)[1] :
        return 1
    else : 
        return 2
