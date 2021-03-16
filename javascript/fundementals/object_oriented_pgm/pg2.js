class Student{
    constructor(name,course){
        this.name=name
        this.course=course
    }
    printStudent(){
        console.log(this.name+','+this.course)
    }
}

var stud= new Student('shaneeba','django')
stud.printStudent()