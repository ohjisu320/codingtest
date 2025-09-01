from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
result = deque()

for _ in range(N) :
    arr_user_input = list(input().split())

    command = arr_user_input[0]
    if command == 'push_front' :
            result.appendleft(arr_user_input[1])
    elif command == 'push_back' :
            result.append(arr_user_input[1])
    elif command == 'front' :
        print(result[0] if result else -1)        
    elif command == 'back' :
        print(result[-1] if result else -1)
    elif command == 'size' :
        print(len(result))
    elif command == 'empty' :
        print(0 if result else 1)
    elif command == 'pop_front' :
        print(result.popleft() if result else -1)
    elif command == 'pop_back' :
            print(result.pop() if result else -1)

