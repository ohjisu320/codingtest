def solution(today, terms, privacies):
    terms_dict = {}
    answer = []
    today_year, today_month, today_day = map(int, today.split("."))
    today = today_year * 12*28 + today_month * 28 + today_day

    for term in terms:
        k, v = term.split(" ")
        terms_dict[k] = int(v)


    for idx, privacy in enumerate(privacies):
        comp_date, term_type = privacy.split(" ")

        comp_year, comp_month, comp_day = map(int,comp_date.split("."))
        comp_date = comp_year *12*28 + comp_month *28 + comp_day

        if today - comp_date  >= terms_dict[term_type] *28:
            answer.append(idx + 1)


    return answer