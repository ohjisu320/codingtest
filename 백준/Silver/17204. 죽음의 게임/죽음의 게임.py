import sys
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())
N_arr = [0] * N

for i in range(N):
    N_arr[i] = int(input())

cnt = 0
next_idx = 0
now_idx = 0
while cnt < N:
    cnt += 1
    now_idx = N_arr[next_idx]
    if now_idx == K:
        print(cnt)
        break
    next_idx = now_idx
else:
    print(-1)