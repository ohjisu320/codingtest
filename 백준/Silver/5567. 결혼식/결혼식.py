# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

def dfs(now, length):
    if dist[now] < length: # 가지치기
        return

    dist[now] = length # 가지치기에 해당하지 않을 때 업데이트

    if length > 2: # 종료조건: 친구의 친구보다 더 멀어지면 종료
        return

    for next in graph[now]: # 현재 인접 리스트에 해당하는 친구 목록 순회
        dfs(next, length + 1) # 현재 인접 리스트에 해당하는 친구1 재귀 호출

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
invite = set()
dist = [float('inf')] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

cnt = 0
for i in range(2, N + 1): # 상근이 제외하고 거리 cnt
    if 0 < dist[i] <= 2:
        cnt += 1

print(cnt)