import sys
input  = lambda :sys.stdin.readline().rstrip()

N = int(input())
wine = [0] + [int(input()) for _ in range(N)]
dp = [[0] * 3 for _ in range(N + 1)]

dp[1][0] = 0       # 1번 술 안 마심
dp[1][1] = wine[1] # 1번 술 1번 연속으로 마심
dp[1][2] = 0       # 1번 술 2번 연속으로 마심 -> 불가능 -> 0

result = 0
for i in range(2, N + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) # i번째 술을 안마셨을 경우 -> 다 됨
    dp[i][1] = wine[i] + dp[i - 1][0]                        # i번째 술을 1번 연속 마셨을 경우 -> i - 1번째에는 안마셔야 함
    dp[i][2] = wine[i] + dp[i - 1][1]                        # i번째 술을 2번 연속 마셨을 경우 -> i - 1번째에는 1번 연속 마셨어야 함

print(max(dp[N][0], dp[N][1], dp[N][2]))