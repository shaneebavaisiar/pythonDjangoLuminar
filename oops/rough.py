class employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name
emp_lst=[]
f=open('employees','r')
for lines in f:
    id,name,desig,exp,salary=lines.rstrip('\n').split(',')
    emp_lst.append(employee(id,name,desig,exp,salary))
salary=[]
for emp in emp_lst:
    salary.append(int(emp.salary))
print(salary)
print(max(salary))


