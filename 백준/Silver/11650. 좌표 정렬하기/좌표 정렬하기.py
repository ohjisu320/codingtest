N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# sort()는 정렬의 우선순위를 정할 수 있다!
arr.sort(key=lambda x : (x[0] ,x[1]))

for a in arr :
    print(*a)
