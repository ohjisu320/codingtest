import sys

input = lambda: sys.stdin.readline().rstrip()


def count_bingo(graph):
    line = 0

    # 1. 가로
    for i in range(5):
        if sum(graph[i]) == 0:
            line += 1
    # 2. 세로
    for i in range(5):
        if sum(graph[j][i] for j in range(5)) == 0:
            line += 1
    # 3. \
    if sum(graph[i][i] for i in range(5)) == 0:
        line += 1
    # 4. /
    if sum(graph[i][4 - i] for i in range(5)) == 0:
        line += 1
    return line

# 철수
cs = [list(map(int, input().split())) for _ in range(5)]

# 사회자
cnt = 0
flag = False
for _ in range(5):
    calls = list(map(int, input().split()))
    for call in calls:
        cnt += 1

        for i in range(5):
            for j in range(5):
                if cs[i][j] == call:
                    cs[i][j] = 0

        if cnt >= 12:
            if count_bingo(cs) >= 3:
                print(cnt)
                flag = True
                break
    if flag:
        break