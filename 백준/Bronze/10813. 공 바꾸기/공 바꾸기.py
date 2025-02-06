N, M= map(int, input().split())

bag= [str(x) for x in range(1,N+1)]

for _ in range(M) :
    i, j = map(int, input().split())
    bag[i-1], bag[j-1] = bag[j-1], bag[i-1]

print(' '.join(bag))