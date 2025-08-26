from collections import deque
import sys

N = int(sys.stdin.readline()) 


q = deque()
for i in range(N) :
    program = sys.stdin.readline().split()
    
    if program[0] == 'push' :
        q.append(int(program[1]))
        
    elif program[0] == 'front' :
        if len(q) > 0 :
            print(q[0])
        else :
            print(-1)
    elif program[0] == 'back' :
        if len(q) > 0 :
            print(q[-1])
        else :
            print(-1)
    elif program[0] == 'size' :
        print(len(q))
    elif program[0] == 'empty' :
        if len(q) > 0 :
            print(0)
        else :
            print(1)
    elif program[0] == 'pop' :
        if len(q) > 0 :
            print(q.popleft())
        else :
            print(-1) 
