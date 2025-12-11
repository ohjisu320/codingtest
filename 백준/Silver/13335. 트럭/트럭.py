from collections import deque
import sys
input  = lambda :sys.stdin.readline().rstrip()

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)

seconds = 0
now_w = 0
while trucks or now_w > 0:
    seconds += 1
    exited_truck = bridge.popleft() # 다리 맨 앞 트럭 빠져나옴
    now_w -= exited_truck           # 다리 하중에서 해당 트럭 무게 빼기
    if trucks:                      # 트럭이 남아있으면
        next_truck = trucks[0]
        if now_w + next_truck <= L:
            trucks.popleft()
            bridge.append(next_truck)
            now_w += next_truck
        else:
            bridge.append(0)

print(seconds)