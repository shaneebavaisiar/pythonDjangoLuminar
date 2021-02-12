# lectrue 25
# q1:print employee details whose designation  developer
# q2:print no of employees as developr
# q3:highest salary

class employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig= desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name

f=open('employee','r')
emplst=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip('\n').split(',')
    emplst.append(employee(id,name,desig,exp,salary))

# print employee details whose designation  developer
devolper=list(filter(lambda emp:emp.desig=='developer',emplst))
for dev in devolper:
    print(dev)

# print no of employees as developr
number_employee_developer=len(list(filter(lambda emp:emp.desig=='developer',emplst)))
print(number_employee_developer)

# highest salary
maxsal=max(list(map(lambda emp:int(emp.salary),emplst)))
print(maxsal)