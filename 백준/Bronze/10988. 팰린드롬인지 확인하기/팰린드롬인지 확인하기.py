s=input()

answer = 0
for i in range(round(len(s)/2)) :
    if s[i] == s[-(i+1)] :
        answer += 1

if answer >= int(len(s)/2) :
    print(1)
else : 
    print(0)
