import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    input_data = list(input())
    stack = []
    flag = True
    for data in input_data:
        if data == '(':
            stack.append(data)
        else:
            if not stack:
                flag = False
                break
            stack.pop()
    result = "YES" if flag and not stack else "NO"
    print(result)

