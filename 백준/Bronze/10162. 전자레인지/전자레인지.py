keys = [A, B, C] = 300, 60, 10
N = int(input())

micro = {A: 0, B: 0, C: 0}

for key in keys :
    while N > 0 :
        N -= key
        if N >= 0 :
            micro[key] += 1
        else :
            N += key
            break
else :
    if N == 0  :
        print(*list(micro.values()))
    else :
        print(-1)