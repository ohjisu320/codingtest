import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0
stack = []

for x, y in arr :
    while stack and stack[-1] > y : # 지금 높이보다 높은 건물 끝
        stack.pop()
        count += 1
    if y > 0 :                      # 높이가 0보다 크면 건물이 있음
        if (not stack or stack[-1] != y): # stack에 아무것도 없거나, 높이가 다를 때
            stack.append(y)

while stack: # 남아있으면 count에 추가
    stack.pop()
    count += 1

print(count)