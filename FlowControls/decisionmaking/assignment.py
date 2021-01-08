#read 2 numbers
#print true if sum of 2 number is equal to 100  or any one number is 100
#else print false
num1=int(input('enter first value'))
num2=int(input('enter second value'))
add=num1+num2
if((num1==100)|(num2==100)|(add==100)):
    print('true')
else:
    print('false')