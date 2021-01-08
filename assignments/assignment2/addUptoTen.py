# Q: addition upto 10
# 2
# 2+22=24

# 3
# 3+33+333=369
n=int(input('enter the value')) #3

i=0
sum=0
a=0
while(i<=n-1):# 0<=2 1<=2,2<=2
    sum=sum+n*(10**i) # 0+3*1=3 ,3+30=33 ,33+300=333
    a=a+sum
    print(sum)
    i+=1
print('total =',a)
