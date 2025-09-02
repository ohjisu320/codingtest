def check(i, j) :
    if 0<= i < N and 0<= j < N :
        return True
    else :
        return False

def walk(i, j):
    lowest = arr[i][j]
    si, sj = i, j
    for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
        ti, tj = i + di, j + dj
        if check(ti, tj) and arr[ti][tj] < lowest:
            lowest = arr[ti][tj]
            si, sj = ti, tj
    if (si, sj) == (i, j):   # 더 낮은 곳 없음
        return 1
    else:
        return 1 + walk(si, sj)

            

T = int(input())

for tc in range(1, T+1) :

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1

    for i in range(N) :
        for j in range(N) :
            si, sj = i, j
            count = walk(si, sj)
            if result < count :
                result = count
           
                    
    print(f'#{tc} {result}')