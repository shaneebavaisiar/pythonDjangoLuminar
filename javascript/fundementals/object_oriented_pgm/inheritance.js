class Parent{
    m1(){
        console.log('inside parent class')
    }
}

class Child extends Parent{
    m2(){
        console.log('inside the child')
    }
}

var child=new Child()
child.m2()
child.m1()