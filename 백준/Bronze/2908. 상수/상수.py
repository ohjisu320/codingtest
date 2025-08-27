A, B = input().split()

new_A = ''
new_B = ''

for ai in range(len(A)):
    new_A += A[-(ai+1)]
for bi in range(len(B)):
    new_B += B[-(bi+1)]

print(max(int(new_A), int(new_B)))