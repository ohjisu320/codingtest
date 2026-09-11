def solution(participant, completion):
    answer = ""
    dict_p = {}
    dict_c = {}

    for p in participant:
        dict_p[p] = dict_p.get(p, 0) + 1
    for c in completion:
        dict_c[c] = dict_c.get(c, 0) + 1

    for pk, pv in dict_p.items():
        if dict_c.get(pk, 0) == 0 or pv > dict_c.get(pk, 0):
            answer = pk

    return answer