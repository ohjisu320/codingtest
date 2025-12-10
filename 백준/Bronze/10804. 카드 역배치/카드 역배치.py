import sys
input  = lambda :sys.stdin.readline().rstrip()

cards = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())

    reversed = cards[a:b + 1][::-1]

    cards[a:b + 1] = reversed

print(*cards[1:])