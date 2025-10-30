import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 플로이드-워셜... 그게 뭔데
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for item in graph:
    print(*item)
