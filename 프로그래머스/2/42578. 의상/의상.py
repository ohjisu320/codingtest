def solution(clothes):
    default_count = 0
    count = 1
    clothes_dict = {}
    for v, k in clothes:
        clothes_dict[k] = clothes_dict.get(k, 0) + 1
    
        
    for item in clothes_dict.values():
        count *= (item + 1)
        
    
        
    return count - 1