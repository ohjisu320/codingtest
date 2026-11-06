from collections import Counter, defaultdict
from math import ceil

def solution(fees, records):
    
    record_dict = defaultdict(int)
    in_cars = set()
    
    for record in records:
        time, car_num, r_type = record.split(" ")
        
        h, m = map(int, time.split(":"))
        minutes = h*60 + m
        
        if r_type == "IN":
            record_dict[car_num] -= minutes
            in_cars.add(car_num)
        else:
            record_dict[car_num] += minutes
            in_cars.remove(car_num)
    
    answer = []
    
    for car_num in sorted(record_dict.keys()):
        minutes = record_dict[car_num]
        if car_num in in_cars:
            minutes += 23 * 60 + 59
        answer.append(cal(minutes, fees))
    
    return answer

def cal(minutes, fees):
    d_t, d_m, e_t, e_m = fees
    
    if minutes <= d_t:
        return d_m
    
    return d_m + ceil((minutes - d_t) / e_t ) * e_m