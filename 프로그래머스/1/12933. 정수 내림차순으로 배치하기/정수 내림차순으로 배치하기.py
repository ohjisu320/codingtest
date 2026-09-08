def solution(n):
    answer = list(str(n))
    return int(''.join(sorted(answer, reverse=True)))