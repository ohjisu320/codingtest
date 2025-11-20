import sys
input = lambda: sys.stdin.readline().rstrip()


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union_find(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return True
    elif rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

    return False



N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    union_find(u, v)

cnt = 0
for i in range(1, N + 1):
    if parents[i] == i:
        cnt += 1
print(cnt)
