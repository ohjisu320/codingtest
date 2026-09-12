def solution(babbling):
    answer = 0

    possible = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        if word in possible:
            answer += 1  # 테스트 1

        else:

            for p_word in possible:  # ["aya", "ye", "woo", "ma"] - "aya"

                if p_word * 2 in word:  # 연속 글자 있으면 안됨 ayaaya
                    break

                if p_word in word:  # 계속 relpace 해도 남아있으면 안됨
                    word = word.replace(p_word, " ")
            else:
                word = word.replace(" ","")
                if not len(word):
                    answer += 1

    return answer
                

            
    return answer