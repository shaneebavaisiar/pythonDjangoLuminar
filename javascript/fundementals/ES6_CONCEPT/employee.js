class Employee{
    constructor(eid,name,sal,desig){
        this.eid=eid
        this.name=name
        this.sal=sal
        this.desig=desig
    }
    printDetails=()=>{
        console.log(this.eid+this.name+this.sal);
    }
}


var employee=[]
var ob=new Employee(100,'varun',25000,'developer')
var ob1= new Employee(101,'dora',22000,'developer')
var ob2= new Employee(102,'buji',23000,'qa')
var ob3=new Employee(103,'harry',27000,'qa')
employee.push(ob)
employee.push(ob1)
employee.push(ob2)
employee.push(ob3)
// to print all desig
employee.forEach(emp=>console.log(emp.desig))

// to add 2000 bonus for all employee
employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal))

// convert employee name into upper case

employee.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name))

// print employee details who have the desig is developer

employee.filter(emp=>emp.desig=='developer').forEach(emp=>console.log(emp))


// sort employee based on their salary
employee.sort((o1,o2)=>o1.sal>o2.sal?1:-1).forEach(emp=>console.log(emp))

// lowest salary from employee
var min_salary=employee.map(ob=>ob.sal).reduce((sal1,sal2)=>sal1>sal2?sal2:sal1)
console.log(`min salary is ${min_salary}`)




