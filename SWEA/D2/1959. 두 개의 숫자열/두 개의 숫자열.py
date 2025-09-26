T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M :
        long = A
        short = B
        len_long = len(A)
        len_short = len(B)
    else :
        long = B
        short = A
        len_long = len(B)
        len_short = len(A)
    max_sum = 0
    for i in range(len_long - len_short + 1):
        now_sum = 0
        for j in range(len_short):
            now_sum += long[i + j] * short[j]
        max_sum = max(max_sum, now_sum)
    print(f"#{tc} {max_sum}")