import sys
input = sys.stdin.readline

def f(n) :
    if memo[n] != -1 :
        return memo[n]
    memo[n] = f(n-1) + f(n-2)
    return memo[n]
    
k = int(input())
memo = [0, 1] + [-1] * (k-1)
print(f(k))