# question:18th lecture

# print_data(rol=1000) then print name of student rol=1000
# print_data(rol=1001,property='course') then print name and course
# ==========================================================================================
f=open('students','r')

student={}
for lines in f:
    id,name,total,course=lines.rstrip('\n').split(',')
    if id not in student:
        student[id]={'name':name,'total':total,'course':course}
print(student)

def print_data(**kwargs):
    print(kwargs)
    id=str(kwargs['id'])
    print(type(id))
    print(id)
    if id in student:
        print(student[id]['name'])
        if 'property' in kwargs:
            property=kwargs['property']
            print(student[id][property])
        else:
            pass
    else:
        print('student doesnot exist with this id')
print_data(id=1001,property='total')




