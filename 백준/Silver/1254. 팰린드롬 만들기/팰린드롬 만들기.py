import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()

for i in range(len(s)):
    sub_string = s[i:]
    if sub_string == sub_string[::-1]:
        print(len(s) + i)
        break