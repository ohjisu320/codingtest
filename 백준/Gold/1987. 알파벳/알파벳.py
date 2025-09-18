import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(now_dist, i, j) :
    global max_dist
    max_dist = max(max_dist, now_dist)
    for di, dj in dirs :
        ni, nj = i + di, j + dj

        if not (0 <= ni < R and 0 <= nj < C) : # 범위 체크
            continue
        next_idx = ord(graph[ni][nj]) - ord('A') # 알파벳을 숫자로 변환해서 idx로 사용
        if visited[next_idx] : # 방문 체크
            continue
        visited[next_idx] = True  # 방문 표시
        dfs(now_dist + 1, ni, nj) # 재귀 호출
        visited[next_idx] = False # 방문 취소


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

visited = [False] * 26 # set 대신 26칸짜리 리스트 사용 (알파벳 26자)
visited[ord(graph[0][0]) - ord('A')] = True # 출발지점 방문 체크
max_dist = 1               # 그래서 거리도 1

dfs(now_dist=1, i=0, j=0)  # 함수 호출
print(max_dist)