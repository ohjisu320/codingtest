# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
triangle = []
dp = []
for i in range(N):
    triangle.append(list(map(int, input().split())))
    dp.append([0] * (i + 1))

dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i + 1):
        # 맨 왼쪽, 맨 오른쪽일 땐 값이 정해져 있음
        if j == 0: # 맨 왼쪽
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i: # 맨 오른쪽
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])

print(max(dp[N - 1]))
