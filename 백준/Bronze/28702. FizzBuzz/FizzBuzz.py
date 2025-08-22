arr = [input() for _ in range(3)]

default = []
for i, a in enumerate(arr) :
    if a.isdigit() :
        default.append([i, int(a)])

if default[-1][0] == 2 :
    result = default[-1][1] + 1
elif default[-1][0] == 1 :
    result = default[-1][1] + 2
else :
    result = default[-1][1] + 3

print('FizzBuzz' if result%15==0 else 'Fizz' if result%3 == 0 else 'Buzz' if result%5 == 0 else result)