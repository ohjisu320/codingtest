# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    middle = N // 2
    result = []
    if N == 1: print(1)
    else:
        for n in range(9, 1, -1): # 9~2까지
            while N % n == 0: # 나누어지면, 나누어질 때 까지
                N = N // n
                result.append(n)

        if N == 1:
            print(len(result))
        else:
            print(-1)