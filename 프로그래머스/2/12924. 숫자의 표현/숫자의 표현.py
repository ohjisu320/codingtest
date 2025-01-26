def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):  # 1부터 √n까지 약수 찾기
        if n % i == 0:
            if i % 2 == 1:  # i가 홀수인지 확인
                answer += 1
            if (n // i) % 2 == 1 and i != n // i:  # n/i도 약수이고 홀수인지 확인
                answer += 1
    return answer