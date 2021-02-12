class employee:
    def __init__(self,id,name,salary,designation):
        self.id=id
        self.name=name
        self.salary=salary
        self.designation=designation
    def get_employee(self):
        print(self.id,',',self.name,',',self.salary,',',self.designation)

ob=employee(1000,'shaneeba',2000,'devloper')
ob.get_employee()