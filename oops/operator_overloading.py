class book(object):
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return book(self.pages+other.pages)
    def __sub__(self, other):
        return book(self.pages + other.pages)
    def __mul__(self, other):
        return book(self.pages * other.pages)

    def __str__(self):
        return str(self.pages)
ob=book(100)
ob1=book(200)
ob2=book(300)
ob3=book(300)
print(ob)
print(ob+ob1+ob2+ob3)
print(ob-ob1)
print(ob-ob1-ob2)
print(ob*ob1*ob2)
