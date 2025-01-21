def solution(lottos, win_nums):
    answer = []
    win = 0
    dn = 0
    for lotto in lottos :
        if lotto == 0 :
            dn +=1
        elif lotto in win_nums :
            win += 1
#   key = win : value = grade     
    win_dict = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    answer = [win_dict[win+dn], win_dict[win]]
        
    return answer

        
    return answer