T = int(input())

for _ in range(T) :
    N = int(input())
    numbers = [input() for _ in range(N)]
    # sort하면 일관성 있는 숫자들끼리 붙는다
    numbers.sort()

    result = 'YES'
    for i in range(N - 1) :
        if numbers[i] == numbers[i + 1][:len(numbers[i])] :
            result = 'NO'
            break
    print(result)