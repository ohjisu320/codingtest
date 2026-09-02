def solution(n):
    list_num = list(str(n))
    answer = 0
    for num in list_num: answer += int(num)
    return answer