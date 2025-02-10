set = [1, 1, 2, 2, 2, 8]
test = list(map(int, input().split()))
result = []

for i in range(len(test)) :
    result.append(str(set[i] - test[i]))

print(' '.join(result) )