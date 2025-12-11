import sys
input  = lambda :sys.stdin.readline().rstrip()

S = set()
M = int(input())
for i in range(M):
    userinput = list(input().split())
    if len(userinput) == 1:
        if userinput == ['all']:
            S = set(range(1, 21))
        else:
            S = set()

    else:
        cmd, x = userinput
        x = int(x)
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            if x in S: S.remove(x)
        elif cmd == 'check':
            if x in S: print(1)
            else: print(0)
        elif cmd == 'toggle':
            if x in S: S.remove(x)
            else: S.add(x)
