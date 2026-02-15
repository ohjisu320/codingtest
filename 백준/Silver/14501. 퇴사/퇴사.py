
import sys
input = sys.stdin.readline

N = int(input())
TP = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(1, N + 1):
    # 상담 안함
    dp[i] = max(dp[i], dp[i - 1])

    # 상담 함
    t, p = TP[i - 1]
    end = i - 1 + t
    if end <= N:
        dp[end] = max(dp[end], dp[i - 1] + p)

print(dp[N])