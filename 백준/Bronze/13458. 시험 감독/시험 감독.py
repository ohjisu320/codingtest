"""
재활훈련...

i번 시험장에 있는 응시자의 수는 A[i]명
총감독관의 할당: 한 시험장에서 감시할 수 있는 응시자의 수 B명
부감독관의 할당: 한 시험장에서 감시할 수 있는 응시자의 수 C명

총감독관은 1명만
부감독관은 여러명

일단 총감독은 모든 방에 있어야 하는거겠지?
그럼 needs = N으로 설정
-> assistant만 계산하면 됨
"""
from math import ceil
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 시험장 개수
rooms = list(map(int, input().split())) # 방 별 응시자 수
head_proctor, assistant = map(int, input().split()) # 감독할 수 있는 응시자 수
needs = N

for room in rooms:
    lasts = room - head_proctor
    if lasts > 0:
        # needss += (lasts + assistant - 1) // assistant
        needs += ceil(lasts/assistant) 

print(needs)
    
    