# 전역 변수 정의
import sys
input = lambda : sys.stdin.readline().rstrip()

DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(start_i, start_j) :
    q = [(start_i, start_j)]
    visited[start_i][start_j] = 1

    while q :
        now_i, now_j = q.pop()
        if now_i == M - 1:
            return True
        for di, dj in DIRS :
            new_i, new_j = now_i + di, now_j + dj
            if not (0 <= new_i < M and 0 <= new_j < N) :
                continue
            if visited[new_i][new_j] :
                continue
            if graph[new_i][new_j] :
                continue
            visited[new_i][new_j] = 1
            q.append((new_i, new_j))

    return False

# 사용자 input
M, N = map(int, input().split())

# 공백 없이 들어오는 것.. 주의...
graph = [list(map(int, list(input()))) for _ in range(M)]


# visited 배열 생성
visited = [[0] * N for _ in range(M)]

# 확인 및 출력
for j in range(N) :
    if graph[0][j] :
        continue
    if dfs(0, j) :
        print('YES')
        break
else :
    print('NO')