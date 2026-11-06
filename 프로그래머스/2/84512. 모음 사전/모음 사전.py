def solution(word):
    vs = ['A', 'E', 'I', 'O', 'U']
    result = []
    
    def dfs(s):
        if len(s) > 5:
            return
        if s:
            result.append(s)
        
        for v in vs:
            dfs(s + v)
    
    dfs("")
    return result.index(word) + 1