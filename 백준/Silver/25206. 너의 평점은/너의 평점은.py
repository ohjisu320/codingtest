input_list = [list(map(str,input().split())) for x in range(20)]

final = 0
grade_to_gpa = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
count = 0
class_count = 0
for i in input_list : 
    if i[2] != "P" : 
        final += float(grade_to_gpa[i[2]])* float(i[1])
        count +=1
        class_count += float(i[1])


print(round(final/class_count,6))
