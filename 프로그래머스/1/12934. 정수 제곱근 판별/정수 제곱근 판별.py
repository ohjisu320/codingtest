def solution(n):
    import math
    
    sqrt = math.sqrt(n)
    answer = (sqrt + 1)**2 if sqrt % 1 == 0 else -1
    return answer