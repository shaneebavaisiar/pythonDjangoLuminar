class Student{
    setStudent(name,course){
        this.name=name
        this.course=course
    }
    printStudent(){
        console.log(this.name+','+this.course)
    }
}

var stud= new Student()
stud.setStudent('shaneeba','django')
stud.printStudent()