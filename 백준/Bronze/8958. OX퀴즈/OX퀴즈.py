T = int(input())

for tc in range(T) :
    arr = input()
    i = 1 # 누적합을 세는 인덱스
    j = 0 # 전체 arr를 세는 인덱스
    result = 0
    while True :
        if j == len(arr) : break
        if arr[j] == 'O' :
            result += i
            i += 1
        else :
            i = 1
        j+=1
    print(result)
