def pascal(N, result) :
    if N == 1 :   
        return print(1)
    if N == 2 : 

        return print(1, 1)
    default = [1]
    result = [1, 1] if result is None else result
    for i in range(len(result)-1) :
        default.append(result[i] + result[i+1])
    default.append(1) 
    return default

        
    return pascal(next)


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    result = []
    print(f'#{tc}')
    for i in range(1, N+1) :
        result = pascal(i, result)
        if result is not None : print(*result)
        else : continue
