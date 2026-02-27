import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

q = deque(range(1, N + 1))
result = []

while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    result.append(str(q.popleft()))

print("<" + ", ".join(result) + ">")