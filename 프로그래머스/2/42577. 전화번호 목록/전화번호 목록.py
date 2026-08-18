def solution(phone_book):
    answer = True
    num_set = set()
    for num in phone_book:
        for i in range(len(num)):
            if i == len(num): break
            num_set.add(num[:i])
    
    for phone_num in phone_book:
        if phone_num in num_set:
            answer = False
            break
    return answer