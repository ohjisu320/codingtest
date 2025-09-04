import sys
sys.setrecursionlimit(10**5)

def postorder(T) :
    if T :
        postorder(left.get(T, 0))
        postorder(right.get(T, 0))
        print(T)
    else : return

input = sys.stdin.readline

arr = []

while True :
    try :
        arr.append(int(input().strip()))
    except (ValueError, IndexError):
        break

N = max(arr)

left = {}
right = {}

root = arr[0]
stack = [root]

i = 1

while i < len(arr) :
    v = arr[i]
    current = 0

    while stack and v > stack[-1]:
        current = stack.pop()

    if current != 0:
        right[current] = v
    else:
        parent = stack[-1]
        left[parent] = v

    stack.append(v)
    i += 1

postorder(root)