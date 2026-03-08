import sys
input  = lambda :sys.stdin.readline().rstrip()

DIRS = [[1,0],[0,1],[-1,0],[0,-1]]

def is_valid(i, j):
    return 0 <= i < 5 and 0 <= j < 5


def dfs(i, j, cnt, number):
    if cnt == 6:
        result_set.add(number)
        return

    for di, dj in DIRS:
        ni, nj = i + di, j + dj
        if not is_valid(ni, nj):
            continue
        dfs(ni, nj, cnt + 1, number + str(graph[ni][nj]))

graph = [list(input().split()) for _ in range(5)]

result_set = set()
for i in range(5):
    for j in range(5):
        dfs(i, j,1, graph[i][j])


print(len(result_set))