t = int(input())
char_list = [input() for _ in range(t)]

noun_list = []
cnt = 0

for char in char_list :
    for index, i in enumerate(char) :
        if i not in noun_list or char[index]==char[index-1] :
            noun_list.append(i)
    if len(char) == len(noun_list) :
        cnt += 1
    noun_list = []

print(cnt)