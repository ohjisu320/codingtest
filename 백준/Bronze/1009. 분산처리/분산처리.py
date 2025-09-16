import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    last_a = a % 10

    if last_a == 0: # 10번 컴퓨터임
        print(10)
        continue

    elif last_a in [1, 5, 6]: # 1, 5, 6 이면 그대로 
        print(last_a)
        
    elif last_a in [4, 9]: # 4, 9면 주기가 2, b에 따라 달라짐
        if b % 2 == 0:  # 짝수 제곱
            print((last_a * last_a) % 10)
        else:  # 홀수 제곱
            print(last_a)
        
    else: # 2, 3, 7, 8은 주기가 4
        # b를 4로 나눈 나머지 구하기, 나머지가 0이면 주기상 4번째를 의미
        b = b % 4
        if b == 0:
            b = 4
        print((last_a ** b) % 10)