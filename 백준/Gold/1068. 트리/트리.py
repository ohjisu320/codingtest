import sys
input = sys.stdin.readline

def dfs(target, nodes) :
    # 해당 노드를 -2로 만듦
    nodes[target] = -2
    for i in range(N) :
        if nodes[i] == target : # 현재 노드를 부모로 갖는 자식 노드 찾으면
            dfs(i, nodes)       # 자식, 자식의 자식, 자식의 자식의 자식도 -2로 만듦


N = int(input())
nodes = list(map(int, input().split()))
target = int(input())
cnt = 0

dfs(target, nodes)

for i, node in enumerate(nodes) :
    if node != -2 and i not in nodes:
        cnt += 1

print(cnt)