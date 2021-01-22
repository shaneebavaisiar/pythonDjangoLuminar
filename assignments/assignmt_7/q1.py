# remove failed students from student list
# students=['name1','name2','name3','name4','name5','name4']
# failed_student=['name1','name2']
# ==============================================================
students=['name1','name2','name3','name4','name5','name4']
failed_student=['name1','name2']
stud=set(students)
failed=set(failed_student)
passed_students=stud.difference(failed)
print(list(passed_students))
