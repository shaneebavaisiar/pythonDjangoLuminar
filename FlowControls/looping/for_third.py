# check given number is prime numbr or not?
# prinme nbrs=7(1,7),only 2 factors

num=int(input('enter the number:'))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=flag+1
        break
        
    else:
        flag=0
if flag==0:
    print(num,'is prime')
else:
    print(num,'is not prime')

