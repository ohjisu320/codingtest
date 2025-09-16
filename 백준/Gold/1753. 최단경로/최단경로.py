import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 모든 정점에 대해 최단 경로를 구하는 문제 == 다익스트라
# bfs 처럼 푸는데 가중치를 비교함
# heapq를 씀
def dijkstra(start_node) :
    pq = [(0, start_node)]
    dists[start_node] = 0

    while pq :
        dist, node = heappop(pq)

        if dists[node] < dist :
            continue

        for next_dist, next_node in graph[node] :
            new_dist = dist + next_dist

            # 새로 찍은 거리가 기존 거리보다 더 크거나 같다면 continue
            if dists[next_node] <= new_dist :
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists

V, E = map(int, input().strip().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E) :
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end)) # 단방향

INF = int(21e9)
dists = [INF for _ in range(V + 1)]


dists = dijkstra(K)

for i in range(1, V + 1) :
    if dists[i] == INF :
        print('INF')
    else :
        print(dists[i])
