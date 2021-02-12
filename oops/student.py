class stud:
    def set_student(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def get_student(self):
        print(self.name,self.age,self.course)

ob=stud()
ob.set_student('shaneeba',2,'djang')
ob.get_student()