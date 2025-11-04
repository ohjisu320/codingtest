# 설정
import sys
input = lambda :sys.stdin.readline().rstrip()

# 함수 + 초기설정
def solve(i, j, size):
    default = graph[i][j]
    for si in range(i, i + size):
        for sj in range(j, j + size):
            if not check(si, sj, default):
                new_size = size // 3
                # 1
                solve(i, j, new_size)
                solve(i, j + new_size, new_size)
                solve(i, j + 2 * new_size, new_size)
                # 2
                solve(i + new_size, j, new_size)
                solve(i + new_size, j + new_size, new_size)
                solve(i + new_size, j + 2 * new_size, new_size)
                # 3
                solve(i + 2 * new_size, j, new_size)
                solve(i + 2 * new_size, j + new_size, new_size)
                solve(i + 2 * new_size, j + 2 * new_size, new_size)
                return
    else:
        paper_dict[default] += 1
    return

def check(i, j, default):
    return default == graph[i][j]

paper_dict = {
    -1 : 0,
    0 : 0,
    1 : 0
}

# 인풋
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 함수호출
solve(0, 0, N)
# 출력
for i in paper_dict.values():
    print(i)