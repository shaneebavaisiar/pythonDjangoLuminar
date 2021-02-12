# lecture:23
# find student name who have course name is django and find the total of that student

class stud:
    def __init__(self,id,name,course,total):
        self.name=name
        self.id=id
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

ob=stud(100,'harry','django',140)
ob1=stud(101,'tom','mean',150)
ob2=stud(102,'jack','ml',160)
ob3=stud(103,'jerry','django',170)
lst=[]
lst.append(ob)
lst.append(ob1)
lst.append(ob2)
lst.append(ob3)
print(lst)
total=0
for stud in lst:
    if stud.course=='django':
        print(stud)
        total+=stud.total
print('total',total)
