'''
stack.pop으로 확인
'''
close = {
    ')' : '(',
    ']' : '[',
}
flag = True
while True :
    txt = input()
    if txt == '.' :
        break
    else :
        stack = []
        for char in txt :
            if char in close.values() :
                stack.append(char)
            elif char in close.keys() :
                if close[char] in stack  and stack[-1] == close[char]:
                    stack.pop()
                else :
                    flag = False
                    break
        else :
            if stack == [] :
                flag = True
            else : 
                flag = False
    print('yes' if flag else 'no')


