
def solution(array, commands):
    answer = []

    for start, end, pick in commands:
        answer.append(sorted(array[start - 1:end])[pick - 1])
    return answer
