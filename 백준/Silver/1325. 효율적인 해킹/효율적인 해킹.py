import sys
input  = lambda :sys.stdin.readline().rstrip()
from collections import deque


N, M = map(int, input().split())

adj_lst = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    adj_lst[b].append(a)

max_cnt = 0
result = []
for start_node in range(1, N + 1):
    cnt = 0
    q = deque([start_node])
    visited = [0] * (N + 1)
    visited[start_node] = 1
    while q:
        node = q.popleft()
        cnt += 1
        for next_node in adj_lst[node]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            q.append(next_node)
    if max_cnt < cnt:
        max_cnt = cnt
        result = [start_node]
    elif max_cnt == cnt:
        result.append(start_node)

print(*(result))