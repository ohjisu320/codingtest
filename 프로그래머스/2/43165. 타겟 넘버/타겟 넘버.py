

def solution(numbers, target):
    
    def dfs(i, total):
        nonlocal answer    
        
        if i == len(numbers):
            if total == target:
                answer += 1
            return


        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])
        return
            
    answer = 0
    dfs(0, 0)
    
    return answer