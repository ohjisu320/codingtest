import sys
input = sys.stdin.readline

N = int(input())
arr1 = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

for m in arr2 :
    print(int(m in arr1))