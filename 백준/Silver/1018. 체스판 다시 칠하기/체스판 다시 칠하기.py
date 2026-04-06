answer_list = [
    ['BW' * 4  , 'WB' * 4] * 4,
    ['WB' * 4  , 'BW' * 4] * 4,
]

min_cnt = float('INF')

N, M = map(int, input().split())
board = [input() for _ in range(N)]


for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        # 1: answer_list[0]과 비교
        first_cnt = 0
        # 2: answer_list[1]과 비교
        second_cnt = 0

        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if answer_list[0][r - i][c - j] != board[r][c]:
                    first_cnt += 1
                if answer_list[1][r - i][c - j] != board[r][c]:
                    second_cnt += 1

        min_cnt = min(min_cnt, first_cnt, second_cnt)


print(min_cnt)
