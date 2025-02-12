text_list = [input() for _ in range(5)]
answer = []
for text in text_list :
    for i in range(len(text)) :
        try: 
            answer[i] += text[i]
        except:
            answer.append(text[i])

print(''.join(answer))