# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i -1] + arr[i]

for _ in range(M):
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    if S == 0:
        print(dp[E])
    else:
        print(dp[E] - dp[S - 1])