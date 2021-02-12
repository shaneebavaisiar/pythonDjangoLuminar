class Parent:
    def m1(self):
        print('inside parent1')
class child(Parent):
    def m1(self):
        print('inside child')
class subchild(child,Parent):
    def m3(self):
        print('inside sub child')

obj=subchild()

obj.m1()