def recur(cnt, base_num):
    # 종료조건: cnt == N
    if cnt == N:
        return base_num ** 2

    # cnt를 1 증가, base_num에 2의 cnt 제곱만큼 더하기
    return recur(cnt + 1, base_num + (2 ** cnt))

N = int(input())

print(recur(0, 2))