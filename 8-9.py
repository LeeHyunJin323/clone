print('8-9. 2222934 이현진')



student_tup = (('211101', '최성훈', '010-1234-4500',4.3), ('211102', '김은지', '010-2230-6540',3.9), ('211103', '이세은', '010-3232-7788',4.25))

student_dict = {}
for t in student_tup:
    student_dict[t[0]] = [t[1], t[2] , t[3]]



for k, v in student_dict.items():
    print(f'{{{k} : {v}}}')



sum = 0


for k, v in student_dict.items():
    sum += v[2]

avg = sum/len(student_dict)

print(f'전체 학생의 학점 평균 : {avg:.2f}')
