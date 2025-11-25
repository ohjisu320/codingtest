import sys
input  = lambda :sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # A의 수 N, B의 수 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = j = 0

    cnt = 0
    while 0 <= i < N and 0 <= j < M:
        if A[i] > B[j]:
            i += 1
            cnt += (M - j)
        elif A[i] <= B[j]:
            j += 1
        elif i == 0 or i == N - 1:
            break
    print(cnt)
