croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()

cnt = 0

for cro in croatian_alphabet :
    if cro in s :
        cnt += s.count(cro)
        s = s.replace(cro, " ")

while " " in s :
    s = s.replace(" ", "")

cnt += len(s)

print(int(cnt))