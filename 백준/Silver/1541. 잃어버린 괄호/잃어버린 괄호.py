from collections import deque

def sum_block(cal) :
    return sum(map(int, cal.split('+')))


cal = input()
cal_list = deque(cal.split('-'))
result = sum_block(cal_list.popleft())


for cal in cal_list :
    result -= sum_block(cal)

print(result)