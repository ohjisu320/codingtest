
import sys
input = lambda :sys.stdin.readline().rstrip()

def preorder(T):
    global preorder_str
    preorder_str += T
    if left.get(T):
        preorder(left[T])
    if right.get(T):
        preorder(right[T])
    return

def inorder(T):
    global inorder_str
    if left.get(T):
        inorder(left[T])
    inorder_str += T
    if right.get(T):
        inorder(right[T])
    return

def postorder(T):
    global postorder_str
    if left.get(T):
        postorder(left[T])
    if right.get(T):
        postorder(right[T])
    postorder_str += T
    return


left = {}
right = {}

N = int(input())

for _ in range(N):
    p, l, r = input().split()
    if l != '.':
        left[p] = l
    if r != '.':
        right[p] = r

preorder_str = ''
inorder_str = ''
postorder_str = ''

preorder('A')
inorder('A')
postorder('A')


print(preorder_str)
print(inorder_str)
print(postorder_str)