import sys
input = sys.stdin.readline


def change_switch(status) :
    return 0 if status else 1

N = int(input())
switch_arr = [0] + list(map(int, input().split()))
student_n = int(input())
for _ in range(student_n) :
    gender, switch = map(int, input().split())
    if gender == 1 : #남자이면
        for s in range(switch, N + 1, switch) :
            switch_arr[s] = change_switch(switch_arr[s])

    else : # 여자이면 마주보는 값 안에 있는거 다 바꾸기
        switch_arr[switch] = change_switch(switch_arr[switch])
        i = switch - 1
        j = switch + 1
        while i >= 1 and j <= N and switch_arr[i] == switch_arr[j]:
            switch_arr[i] = change_switch(switch_arr[i])
            switch_arr[j] = change_switch(switch_arr[j])
            i -= 1
            j += 1


for i in range(1, N + 1) :
    print(switch_arr[i], end=" ")
    if i%20 ==0 :
        print()