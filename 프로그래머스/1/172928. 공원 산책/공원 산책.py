def solution(park, routes):
    answer = []
    N = len(park)
    M = len(park[0])
    si, sj = find_start(N, M, park)

    for route in routes:
        op, n = route.split(" ")
        n = int(n)

        now_i, now_j = si, sj
        flag = True
        for _ in range(n):
            di, dj = dir_dict[op]
            
            next_i, next_j = now_i + di, now_j + dj
            if not is_valid(next_i, next_j, N, M):
                break
            if park[next_i][next_j] == "X":
                break
            
            now_i, now_j = next_i, next_j
        
        else:
            si, sj = now_i, now_j
        
    return  [ si, sj ]

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
            if park[i][j] == "S": return i, j