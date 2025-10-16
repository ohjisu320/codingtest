
# 초기값 세팅 + 함수
import sys
input = lambda: sys.stdin.readline().rstrip()


def sum_cost(r, c):
    return grid[r][c] + grid[r-1][c] + grid[r+1][c] + grid[r][c-1] + grid[r][c+1]

def check(r, c, now_locs):
    for prev_r, prev_c in now_locs:
        # 겹치는 지 맨해튼 거리로 확인
        if abs(r - prev_r) + abs(c - prev_c) < 3:
            return False
    else :
        return True


def find_combinations(start_idx, now_locs, now_cost):
    global min_cost

    # 가지치기
    if now_cost > min_cost :
        return

    # 종료 조건: 3개의 위치를 모두 선택했을 때
    if len(now_locs) == 3:
        min_cost = min(min_cost, now_cost)
        return

    for i in range(start_idx, len(locations)):
        r, c = locations[i]
        if check(r, c, now_locs):

            now_locs.append(locations[i])

            find_combinations(i + 1, now_locs, now_cost + sum_cost(r, c))

            now_locs.pop()


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')
locations = []
for r in range(1, N - 1):
    for c in range(1, N - 1):
        locations.append((r, c))


find_combinations(0, [], 0)

print(min_cost)

