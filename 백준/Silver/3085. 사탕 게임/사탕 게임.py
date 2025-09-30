import sys
input = lambda : sys.stdin.readline().rstrip()

DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def find() :
    max_len = 1
    # 모든 행을 검사
    for i in range(N):
        count = 1
        for j in range(N - 1):
            if graph[i][j] == graph[i][j + 1]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)

    # 모든 열을 검사
    for j in range(N):
        count = 1
        for i in range(N - 1):
            if graph[i][j] == graph[i + 1][j]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)
    return max_len


N = int(input())

graph = [list(input()) for _ in range(N)]

max_sum = 0

for i in range(N) :
    for j in range(N) :
        now_color = graph[i][j]
        for di, dj in DIRS :
           ni, nj = i + di, j + dj
           if not (0 <= ni < N and 0 <= nj < N) :
               continue
           if graph[ni][nj] == now_color :
               continue
           graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
           now_sum = find()
           max_sum = max(max_sum, now_sum)
           graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
print(max_sum)