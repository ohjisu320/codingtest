n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
# [[123, 1, 1], [356, 1, 0], ... ]
answer = 0
for a in range(1, 10) : #100의자리수
    for b in range(1, 10) : #10의자리수
        for c in range(1, 10) : #1의자리수
            if (a==b or a==c or b==c) :
                continue
            # 숫자가 정해졌다면
            cnt = 0
            test_num = [a,b,c]
            for arr in hint :
                number = list(map(int, str(arr[0]))) # 123 -> [1,2,3]
                strike = arr[1]
                ball = arr[2]
                # 임의의 숫자 abc가 정답일 때, 예측값과 strike, ball 값이 같아야 정답 -> strike, ball 값 업데이트
                strike_cnt = 0
                ball_cnt = 0
                # 비교하는 부분
                for x in range(3) :
                    if  test_num[x] == number[x] :
                        strike_cnt += 1
                    elif test_num[x] in number:
                        ball_cnt += 1
                # 만약 아래의 조건과 같다면 cnt+1
                if strike == strike_cnt and ball == ball_cnt :
                    cnt += 1
            if cnt == n :
                answer += 1

print(answer)

                
