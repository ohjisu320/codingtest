def solution(brown, yellow):
    import math
    
    for i in range(3, brown + yellow):
        width, height = (brown+yellow)/i, i 

        if yellow == (width - 2) * (height - 2):
            
            return [int(width), height]
    
    