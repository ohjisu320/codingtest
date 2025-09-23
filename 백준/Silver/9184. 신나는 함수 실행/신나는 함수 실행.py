def w(a, b, c) :

    if a <= 0 or b <= 0 or c <= 0 :
        return 1

    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    if memo[a][b][c] :
        return memo[a][b][c]

    if a < b and b < c:
        result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    else:
        result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    # memo에 저장
    memo[a][b][c] = result
    return result

while True :
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break

    memo = [[[0] * 21 for _ in range(21)] for _ in range(21)] # 20보다 크면 20으로 변환하니깐

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
