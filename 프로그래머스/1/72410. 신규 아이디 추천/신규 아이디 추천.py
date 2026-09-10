def solution(new_id):
    new_id = new_id.lower()  # 1단계: 소문자로 변환 / 3단계: ..->.으로 변환

    answer = ''
     # 2단계: 특수문자 삭제
    for id in new_id:
        if  ord('0') <= ord(id) <= ord('9') or ord('a') <= ord(id) <= ord('z') or id in '_.-':
            if id =='.' and answer and answer[- 1] =='.':
                pass
            else:
                answer += id

    answer = answer.strip(".")  # 4단계: 앞뒤 . 삭제

    if answer == '':  # 5단계: 빈 문자열일 경우 "a"
        answer = "a"
    if len(answer) >= 16:  # 6단계: 16자 이상일 경우 15자 이후 문자열 삭제
        answer = answer[:15].strip(".")
        pass

    if len(answer) <= 2:  # 7단계: 2자 이하일 경우 3자가 될 때 까지 맨 뒤 문자 붙이기
        answer += answer[-1] * (3 - len(answer))

    return answer
