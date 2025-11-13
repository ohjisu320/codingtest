# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

lst = input()

q = list()
cnt = 0
for idx, item in enumerate(lst):
    if item == '(': # 레이저 or 쇠막대기
        q.append(item)
    elif item == ')': # 레이저 or 쇠막대기 끝
        q.pop() # 레이저이든 쇠막대기든 둘 다 pop할 것임

        if lst[idx - 1] == '(': # 레이저일 때
            cnt += len(q)
        elif lst[idx - 1] == ')': # 쇠막대기의 끝일 때
            cnt += 1

print(cnt)
