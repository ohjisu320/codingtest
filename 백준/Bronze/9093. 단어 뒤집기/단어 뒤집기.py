import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    str_arr = list(input().split())
    reversed_arr = [item[::-1] for item in str_arr]
    print(' '.join(reversed_arr))