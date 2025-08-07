from pprint import pprint

T = int(input()) 
for tc in range(1, T+1) :
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    idx = N
    i = 0
    j = N-1

    arr[0] = [i+1 for i in range(N)]

    def recursive(size, idx, i, j, loop) :
        di = [1, 0, -1, 0] # arr[0]을 주고 시작하기 때문에
        dj = [0, -1, 0, 1] # 방향은 하 좌 상 우 순으로 진행 
        # N-1 * 2번 반복 -> N-2 * 2번 반복 -> ... 1 * 2번 반복
        for _ in range(2) :         # 2번 반복
            for _ in range(size):   # size == (N-1)만큼 반복
                i += di[(loop%4)] 
                j += dj[(loop%4)]
                idx += 1
                arr[i][j] = idx
            loop += 1               # 작은 for문 끝난 후 방향 바꾸기
                
        if idx == N**2 :            # idx가 N*N일 때 끝남
            return 
        recursive(size-1, idx, i, j, loop)  # 안끝난다면 재귀
        
    recursive(N-1, idx, i, j, 0)
    print(f'#{tc}')
    for a in arr : 
        print(*a) 
        