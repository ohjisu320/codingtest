import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

dance_dict = dict()
for _ in range(N) :
    A, B = input().split()
    dance_dict[A] = dance_dict.setdefault(A, 0)
    dance_dict[B] = dance_dict.setdefault(B, 0)
    if A == 'ChongChong' or B == 'ChongChong' :
        dance_dict[A] = dance_dict[B] = 1
    elif dance_dict[A] or dance_dict[B]:
        dance_dict[A] = dance_dict[B] = 1
        
cnt = 0
for _,value in dance_dict.items() :
    cnt += value
print(cnt)