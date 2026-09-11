def solution(word):
    answer = 0
    chars = ["A", "E", "I", "O", "U"]
    count = 0
    
    def dfs(now_word):
        nonlocal answer, count
        if len(now_word) == 5: # 5글자까지 채워서 만들었으면
            return
        
        if answer: # 정답 있으면
            return
        
        for c in chars:
            next_word = now_word + c # 다음 단어는 하나씩 늘려가는거
            count += 1
            
            if next_word == word:
                answer = count # 지금까지 센 정답 반환
                return
            else:
                dfs(next_word)
            

        
        
    dfs("")
    return answer