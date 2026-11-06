dir_dict = {
    "N": [-1, 0],
    "S": [1, 0],
    "W": [0, -1],
    "E": [0, 1]
}

def is_valid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M

def find_start(N, M, park):
    for i in range(N):
        for j in range(M):
            if park[i][j] == "S":
                return i, j
    return

def solution(park, routes):
    
    N = len(park)
    M = len(park[0])
    si, sj = find_start(N, M, park)
    
    for route in routes:
        op, n = route.split(" ")
        n = int(n)
        flag = True
        next_i, next_j = si, sj
        for i in range(n):
            now_i, now_j = next_i + dir_dict[op][0], next_j + dir_dict[op][1]
            if not is_valid(now_i, now_j, N, M):
                flag = False
                continue
            if park[now_i][now_j] == "X":
                flag = False
                continue
            
            next_i, next_j = now_i, now_j
        if flag:
            si, sj = next_i, next_j
            
            
            

    answer = [si, sj]
    return answer

