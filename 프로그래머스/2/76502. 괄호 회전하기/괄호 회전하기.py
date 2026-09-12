def solution(s):
    count = 0
    
    def is_valid(s):
        pair_dict = {  "]": "[", ")": "(", "}": "{"}
        stack = []
        
        for c in s:

            if c in pair_dict.values():
                stack.append(c)
            else:
                if not stack:
                    return False

                if stack.pop() != pair_dict[c]:
                    return False
        return not stack
    
    for i in range(len(s)):
        if is_valid(s[i:] + s[:i]):
            count += 1
    
    return count
    
        
    
    
    

    
    
    

    
    return answer