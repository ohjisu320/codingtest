import sys
input  = lambda :sys.stdin.readline().rstrip()
import math

T = int(input())
for _ in range(T):
    # 조규현 좌표 (x1, y1), 백승환 좌표 (x2, y2), 조규현이 계산한 거리 r1, 백승환이 계산한 거리 r2
    # 출력: 류재명이 존재할 수 있는 좌표
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if d == 0 and r1 == r2:
        print(-1)
    elif d > r1 + r2 or d < abs(r1 - r2) :
        print(0)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    elif abs(r1 - r2) < d < r1 + r2 :
        print(2)