import sys
input = lambda :sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = input()

result = 0
stack = []
M = K

for num in arr:
    while stack and M > 0 and stack[-1] < num:
        stack.pop()
        M -= 1
    stack.append(num)

print(''.join(stack[0 : N - K]))