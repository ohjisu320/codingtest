import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    k = int(input()) # k는 층,
    n = int(input()) # n은 호
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for k_idx in range(k + 1):
        for n_idx in range(1, n + 1):
            if k_idx == 0:
                dp[0][n_idx] = n_idx
            else:
                dp[k_idx][n_idx] = dp[k_idx][n_idx - 1] + dp[k_idx - 1][n_idx]
    print(dp[k][n])