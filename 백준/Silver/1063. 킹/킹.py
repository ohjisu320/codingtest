import sys
input = lambda :sys.stdin.readline().rstrip()

move_dict = {
    'R':(1, 0),
    'L':(-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1),
}

king, stone, N = input().split()

king_x, stone_x = ord(king[0]) - 64, ord(stone[0]) - 64
king_y, stone_y = int(king[1]), int(stone[1])
N = int(N)

for _ in range(N):
    path = input()
    dx, dy = move_dict[path]

    new_king_x = king_x + dx
    new_king_y = king_y + dy

    if not (0 < new_king_x <= 8) or not (0 < new_king_y <= 8):
        continue

    if new_king_x == stone_x and new_king_y == stone_y:
        # 겹칠 때
        new_stone_x = stone_x + dx
        new_stone_y = stone_y + dy

        if not (0 < new_stone_x <= 8) or not (0 < new_stone_y <= 8):
            continue

        king_x, king_y = new_king_x, new_king_y
        stone_x, stone_y = new_stone_x, new_stone_y
    else:
        # 겹치지 않을 때
        king_x, king_y = new_king_x, new_king_y

king, stone = str(chr(king_x + 64)) + str(king_y), str(chr(stone_x + 64)) + str(stone_y)
print(king)
print(stone)


