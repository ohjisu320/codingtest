import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())

dp = [[0] * 3 for _ in range(N)]

costs = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째는 가격 정해놓고 시작
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1, N):
    # 빨강
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])

    # 초록
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])

    # 파랑
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))