N, M = map(int, input().split())

poketmon = {}

for i in range(N) :
    name = input()
    poketmon.update({str(i+1) : name})
    poketmon.update({name: i + 1})

for _ in range(M) :
    print(poketmon[input()])