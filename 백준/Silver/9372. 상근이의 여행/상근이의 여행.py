import sys
input = lambda :sys.stdin.readline().rstrip()

def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x, y):
    pre_x = find_set(x)
    pre_y = find_set(y)

    if pre_x == pre_y:
        return False
    elif pre_x < pre_y:
        parent[pre_y] = pre_x
    else:
        parent[pre_x] = pre_y
    return True


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    edge_count = 0
    for _ in range(M):
        a, b = map(int, input().split())
        if union_set(a, b):
            edge_count += 1

    print(edge_count)
