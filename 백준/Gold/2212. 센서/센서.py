N = int(input())
K = int(input())

if K >= N :
    print(0)
else :
    arr = list(map(int, input().split()))
    arr.sort()
    
    dist = []
    for idx in range(N - 1) :
        dist.append(arr[idx + 1] - arr[idx])
    
    dist.sort(reverse=True)
    
    for _ in range(K - 1) :
        dist.pop(0)
    
    print(sum(dist))