# Q:3
# 321=123
# ======================
import math
n=int(input('enter the value')) #3
k=math.log10(n)+1
t=math.floor(k)
# print('length=',t)

i=1

while(i<=t): #123
    a=n%10 #3
    print(a,end='')
    b=n//10
    n=b
    # print(b)
    i+=1
# b=1//10
# if b==0:


