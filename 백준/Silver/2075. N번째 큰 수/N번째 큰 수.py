# 초기설정
import sys, heapq
input = lambda :sys.stdin.readline().rstrip()

N = int(input())

for i in range(N):
    if i == 0: # 첫 번째는 그냥 heapify로 heap 만들기
        hq = list(map(int, input().split()))
        heapq.heapify(hq)
        continue
    arr = list(map(int, input().split())) # 그 다음부턴 비교하기
    for item in arr:
        if item > hq[0]:
            heapq.heappushpop(hq, item)

print(hq[0])