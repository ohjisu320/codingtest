default = input()
pop = list(input())

stack = []
len_pop = len(pop)
for char in default:
    stack.append(char)

    if len(stack) >= len_pop and stack[-len_pop:] == pop:
        del stack[-len_pop:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")