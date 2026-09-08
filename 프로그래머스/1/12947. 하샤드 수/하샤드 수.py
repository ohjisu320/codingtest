def solution(x):
    list_num = list(map(int, str(x)))
    m = sum(list_num)
    
    return x % m == 0