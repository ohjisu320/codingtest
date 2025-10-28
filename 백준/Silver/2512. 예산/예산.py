import sys
input = sys.stdin.readline


N = int(input())
local_budget = list(map(int, input().split()))
total_budget = int(input())

local_budget.sort()

if total_budget >= sum(local_budget):
    print(local_budget[-1])
else:
    start = 0
    end = local_budget[-1]
    result_budget = 0

    while start <= end:
        mid = (start + end) // 2
        temp_sum = 0
        for local in local_budget:
            if local <= mid:
                temp_sum += local
            else:
                temp_sum += mid

        if temp_sum <= total_budget:
            result_budget = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result_budget)