#find three number and find heighst number
#find second largest number 40?
#sort these three numbers 30 40 50?

num1=int(input('enter num1'))
num1=int(input('enter num2'))
num1=int(input('enter num3'))
if((num1>num2)&(num1>num3)):
    print('num1 is largest')
elif((num2>num1)&(num2>num3)):
    print('num2 is largest')
elif((num3>num1)&(num3>num2)):
    print('num3 is largest')
elif((num1==num2)&(num1==num3)):
    print('three numbrs are equal')
