from collections import  deque

N = int(input())
balloons_input = list(map(int, input().split()))
balloons = deque(enumerate(balloons_input, 1)) # enumerate로 (idx, item) 형태 만들어주기
result = []

while balloons:
    idx, target = balloons.popleft() # prev = idx, target = balloons.popleft()

    result.append(idx) 

    if not balloons: # popleft() -> result.append 과정 끝난 후 balloons이 없으면 종료
        break

    dir = - 1 if target > 0 else 0 # target이 양수일 땐 보정 필요(prev 포함됨), 음수일 땐 보정 불필요(prev 포함 안됨)
    balloons.rotate(-(target + dir)) # balloons.rotate(양수) -> 오른쪽으로 회전, (음수) -> 왼쪽으로 회전

print(*result)
