# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

def reverse(graph, r_range, c_range):
    for r in r_range:
        for c in c_range:
            if graph[r][c] == '1':
                graph[r][c] = '0'
            else:
                graph[r][c] = '1'
    return graph

N,M = map(int, input().split())
graph_a = [list(input()) for _ in range(N)]
graph_b = [list(input()) for _ in range(N)]


cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if graph_a[i][j] == graph_b[i][j]:
            continue
        graph_a = reverse(graph_a, range(i, i + 3), range(j, j + 3))
        cnt += 1

print(cnt if graph_a==graph_b else -1)