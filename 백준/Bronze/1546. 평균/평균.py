N = int(input())
list = list(map(int, input().split()))

M = max(list)
print(sum(list)*100 / M / int(N))
