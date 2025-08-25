C = int(input())
for tc in range(C) :
    N, *students = list(map(int, input().split()))
    sum_student = 0
    for student in students :
        sum_student += student
    mean_student = sum_student/N
    result = 0
    for student in students :
        if student > mean_student :
            result += 1
    print(f'{(result/N)*100: .3f}%')