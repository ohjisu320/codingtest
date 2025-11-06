# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
books = [int(input()) for _ in range(N)]

cnt = 0

target = N

for i in range(N - 1, -1, -1):
    if books[i] == target:
        cnt += 1
        target -= 1

print(N - cnt)