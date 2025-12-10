import sys
input  = lambda :sys.stdin.readline().rstrip()

def compress(x, y, n):
    default = grid[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != default:
                half_n = n // 2

                result = '('

                # 왼쪽 위
                result += compress(x, y, half_n)

                # 오른쪽 위
                result += compress(x, y + half_n, half_n)

                # 왼쪽 아래
                result += compress(x + half_n, y, half_n)

                # 오른쪽 아래
                result += compress(x + half_n, y + half_n, half_n)

                result += ')'
                return result

    return str(default)

N = int(input())
grid = [list(input()) for _ in range(N)]

if grid == [['0'] * N for _ in range(N)]: print(0)
elif grid == [['1'] * N for _ in range(N)]: print(1)
else:
    print(compress(0, 0, N))
