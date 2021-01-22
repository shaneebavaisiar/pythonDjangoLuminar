# find passed students by using students and fail file

student_file=open('students','r')
students=[]

for stud in student_file:
    students.append(stud.rstrip('\n'))
print('students:',students)

failed_file=open('fail','r')
failed=[]

for fail in failed_file:
    failed.append(fail.rstrip('\n'))
print('failed students:',failed)

passed_students=set(students).difference(set(failed))
print('passed students:',list(passed_students))

