def solution(s):
    answer = ''
    answer_list = list(map(int, s.split()))
    answer_list.sort()
    answer += str(answer_list[0])
    answer += " "+str(answer_list[-1])
    return answer