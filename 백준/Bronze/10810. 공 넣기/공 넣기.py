N, M= map(int, input().split())

bag= ['0' for x in range(1,N+1)]

change_list = [list(map(int, input().split())) for _ in range(M)]
for change in change_list :
    start = change[0]-1
    end = change[1]
    number = change[2]
    bag[start:end] = [str(number) for _ in range(end-start)]
    pass

print(' '.join(bag))
