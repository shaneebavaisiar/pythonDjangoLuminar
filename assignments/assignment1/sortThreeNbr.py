#sort these three numbers 30 40 50?
a=int(input('enter num1'))
b=int(input('enter num2'))
c=int(input('enter num3'))
if(a<b<c):
    print(a,b,c)
elif(a<c<b):
    print(a,c,b)
elif (b < a < c):
    print(b, a, c)
elif (b < c < a):
    print(b, c, a)
elif (c < a < b):
    print(c, a, b)
else:
    print(c,b,a)