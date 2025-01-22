def solution(survey, choices):
    answer = ''
    dict = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for index, sur in  enumerate(survey) :
        if choices[index] > 4 :
            type = sur[1]
            dict[type] += (choices[index]-4)
        elif choices[index] < 4:
            type = sur[0]
            dict[type] += (4-choices[index])
        else :
            pass
    list = ["R", "T", "C", "F", "J", "M", "A", "N"]
    for i in range(4) :

        if dict[list[2*i]] >= dict[list[2*i+1]] :
            answer += list[2*i]
        else : 
            answer += list[2*i+1]
        

    
    return answer