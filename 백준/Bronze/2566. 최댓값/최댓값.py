matrix = [list(map(int, input().split()))for _ in range(9)]
maximum = 0
location = [0, 0]
for y in range(len(matrix)) :
    for x in range(len(matrix))  :
        if matrix[x][y] >= maximum :
            maximum = matrix[x][y]
            location[0] = x
            location[1] = y

print(maximum)
print(str(location[0]+1), str(location[1]+1))
pass