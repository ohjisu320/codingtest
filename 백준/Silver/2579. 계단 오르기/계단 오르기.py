# dp문제
"""
Docstring for BOJ.PYTHON.boj2579


dp[i][0]: 해당 num을 포함하지 않음
dp[i][1]: 해당 num을 1회 포함함
dp[i][2]: 2 연속 포함함

마지막 계단은 무조건 밟음
"""

import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())

dp = [[0]  * 3 for _ in range(N)]
 

for i in range(N):
    num = int(input())    
    if i: 
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = dp[i - 1][0] + num
        dp[i][2] = dp[i - 1][1] + num
        
    else:
        dp[i][0] = 0 # 첫번째 계단 패스 -> 다음 계단을 무조건 밟음
        dp[i][1] = dp[i][2] = num


print(max(dp[N - 1][1], dp[N - 1][2]))