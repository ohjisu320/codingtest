# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N, K, Q, M = map(int, input().split())
sleep_students = set(map(int, input().split()))
code_students = set(map(int, input().split()))

# 출석표 - 일단 출석했다 치고 시작
checked = [1] * (N + 3)

for code_student in code_students:
    # 코드 받은 애가 조는 애 중에 있으면 넘어가기
    if code_student in sleep_students:
        continue
    # 안졸면 자기 배수에 해당하는 데에 체크
    for i in range(code_student, N + 3, code_student):
        # 배수가 조는지 확인
        if i in sleep_students:
            continue
        checked[i] = 0

for _ in range(M):
    S, E = map(int, input().split())
    print(sum(checked[S:E + 1]))
