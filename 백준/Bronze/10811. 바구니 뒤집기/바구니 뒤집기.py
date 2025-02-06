N, M= map(int, input().split())

bag= [str(x) for x in range(1,N+1)]

for _ in range(M) :
    i, j = map(int, input().split())
    in_list = list(range(i-1, j))
    for index in in_list[:int(len(in_list)/2)] :
        bag[index], bag[i+j-index-2] = bag[i+j-index-2], bag[index]
        pass
    
print(' '.join(bag))