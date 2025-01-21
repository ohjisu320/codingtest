def solution(participant, completion):
    part_dict = {}
    answer = ""
#     participant를 딕셔너리에 저장
    for part in participant :
        part_dict[part] = part_dict.get(part, 0) +1
#     저장된 딕셔너레에서 competion에 포함된 사람의 value-1
    for comp in completion :
        part_dict[comp] -= 1
#     value가 0보다 큰 사람(잔여 선수)를 answer에 저장
    for key, value in part_dict.items() :
        if value > 0 :
            answer = key
    
    return answer