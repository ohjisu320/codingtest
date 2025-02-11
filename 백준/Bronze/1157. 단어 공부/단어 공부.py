from collections import Counter

s_list = list(map(str, input().lower()))
dict = Counter(s_list)

key_list = []
def solution(dict) :
    for key, value in dict.items() :
        if max(dict.values()) == value :
            key_list.append(key)
    if len(key_list) > 1 :
        return print("?")
    else :
        return print(key_list[0].upper())

solution(dict)