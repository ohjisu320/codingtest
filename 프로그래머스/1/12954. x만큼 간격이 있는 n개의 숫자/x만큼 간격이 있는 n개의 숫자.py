def solution(x, n):
    answer = [x,]
    now = x
    for i in range(n - 1):
        now += x
        answer.append(now)
    return answer