import sys
input = lambda :sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    # N일 동안....
    chart = list(map(int, input().split()))
    total_price = 0
    now_price = 0
    for i in range(N-1, -1, -1):
        if chart[i] > now_price:
            now_price = chart[i]

        else:
            total_price += (now_price - chart[i])


    print(total_price)