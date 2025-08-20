N = int(input())
num_list = [0] * 10001
for i in range(N) :
    num_list[int(input())] += 1
for idx, item in enumerate(num_list) :
    if item :
        for _ in range(item) :
            print(str(idx)) 

