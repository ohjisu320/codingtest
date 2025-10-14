import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i): # i의 이전거랑 비교
        if arr[j] > arr[i]:
            # 값 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))