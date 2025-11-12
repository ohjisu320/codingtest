import sys
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())

INF = float('inf')

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    result = INF
    result_idx = -1
    for i in range(1, N + 1):
        now_result = 0
        for j in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            now_result += graph[i][j]
        if result > now_result:
            result = now_result
            result_idx = i
print(result_idx)