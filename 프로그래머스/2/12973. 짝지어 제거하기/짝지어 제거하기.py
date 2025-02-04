def solution(s):
    stack = []
    for char in s :
        if stack and stack[-1] == char :
            stack.pop()
        else :
            stack.append(char)

    return 1 if stack ==[] else 0