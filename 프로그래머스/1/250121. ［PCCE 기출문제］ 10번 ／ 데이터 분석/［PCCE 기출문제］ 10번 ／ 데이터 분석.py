def solution(data, ext, val_ext, sort_by):
    answer = []
    q_list = ["code", "date", "maximum", "remain"]
    ext_question = q_list.index(ext)
    sort_question = q_list.index(sort_by)

    
    for index, d in enumerate(data) :
        if d[ext_question] < val_ext :
            answer.append(d)



    return sorted(answer, key=lambda x: x[sort_question])