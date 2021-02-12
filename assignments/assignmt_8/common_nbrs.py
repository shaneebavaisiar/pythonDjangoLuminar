num1=[9,5,3,5,6,7,2,1]
num2=[1,2,4,8,9]
common=list(filter(lambda x:x in num2,num1))
print(common)