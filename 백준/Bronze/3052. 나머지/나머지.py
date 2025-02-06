from collections import Counter

input_list = [int(input())%42 for _ in range(10)]
input_dict = dict(Counter(input_list))

print(10-(len(input_list)-len(input_dict)))
        