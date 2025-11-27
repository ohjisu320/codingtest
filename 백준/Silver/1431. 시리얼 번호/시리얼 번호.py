# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
arr = [input() for _ in range(N)]

def find_num(str):
    num_sum = 0
    for char in str:
        if char.isdigit():
            num_sum += int(char)
    return num_sum


arr.sort(key=lambda x: (len(x), find_num(x), x))

print(*arr, sep='\n')