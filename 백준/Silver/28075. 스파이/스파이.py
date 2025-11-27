# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()


def spy(cnt, now_sum, pre_loca):
    global result
    if now_sum >= M:
        result += pow(6, N - cnt) # 남은 날의 경우의 수
        return

    if cnt == N:
        if now_sum >= M:
            result += 1
        return

    for loca in range(3):
        for work in range(2):
            add_sum = grid[work][loca]
            if loca == pre_loca:
                add_sum /= 2
            spy(cnt + 1, now_sum + add_sum, loca)


N, M = map(int, input().split()) # N일 동안 M을 얻기 == N일 동안 M을 얻을 수 있는 방법 모두 구하기

grid = [list(map(int, input().split())) for _ in range(2)]

# (0, 0), (0, 1) => 이런 식으로 장소 값이 같으면 절반!
result = 0

spy(0, 0, -1)

print(result)
