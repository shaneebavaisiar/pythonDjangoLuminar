# lecture:23
# q1:print employee details whose designation  developer
# q2:print no of employees as developr
# q3:print employee details who have heighst salary
# q4:print heighest salary person name whose designation is developer
class Employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name


f=open('employees','r')
emplist=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip('\n').split(',')
    emplist.append(Employee(id,name,desig,exp,salary))
total=0
salary_lst=[]
dev_salary_lst=[]
developer_lst=[]
for employee in emplist:
    if employee.desig=='developer':
        dev_salary_lst.append(int(employee.salary))
        developer_lst.append(employee)
        total+=1
        print(employee)
print('total employess whose designation developer:',total)
heighest_salary_developer=max(dev_salary_lst)

for employee in emplist:
    salary_lst.append(int(employee.salary))

heighest_salary=max(salary_lst)
print('heighest salary:',heighest_salary)

for employee in emplist:
    if employee.salary==heighest_salary:
        print('heigest salary person name:',employee.name)

for employee in developer_lst:
    if int(employee.salary)==heighest_salary_developer:
        print('heighest salary has developer:',employee.name)
