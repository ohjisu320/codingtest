from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()


N = int(input())
ta, tb = map(int, input().split()) # 촌수를 계산해야 하는 번호
M = int(input()) # 부모자식 관계의 수

adj_lst = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split()) # p:부모, c:자식
    adj_lst[p].append(c)
    adj_lst[c].append(p)

visited = [-1] * (N +1)

q = deque([ta])
visited[ta] = 0
while q:
    now = q.popleft()
    if now == tb:
        print(visited[tb])
        break
    for next in adj_lst[now]:
        if visited[next] != -1:
            continue
        visited[next] = visited[now] + 1
        q.append(next)
else:
    if visited[tb] == -1:
        print(-1)
    else:
        print(visited[tb])