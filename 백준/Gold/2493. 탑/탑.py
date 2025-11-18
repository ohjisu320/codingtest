# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
towers = list(map(int, input().split()))

stack = []
answer = []

for i in range(N):
    current_height = towers[i]

    while stack:
        # 나보다 작은 탑 만나면
        if stack[-1][0] < current_height:
            stack.pop()
        else:
            # 나보다 크거나 같은 탑 만나면
            break

    if stack:
        # 스택에 나한테 수신할 (나보다 큰) 탑 있으면
        answer.append(stack[-1][1])
    else:
        # 스택이 비었으면
        answer.append(0)

    stack.append((current_height, i + 1))

print(*answer)
