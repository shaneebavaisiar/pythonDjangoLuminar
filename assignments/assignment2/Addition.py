#Q:1
# 2
# 2+22=24

# 3
# 3+33+333=369
# =======================================
import math
num=int(input('enter the value')) #3
k=math.log10(num)+1
t=math.floor(k)
print('length=',t)
i=0
sum=0
total=0
while(i<=num-1):# 0<=2 1<=2,2<=2
    sum = sum+num*(10**(i*t)) # 0+3*1=3 ,3+30=33 ,33+300=333
    total=total+sum
    print(sum)
    i+=1
print('total =',total)
