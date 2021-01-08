#123
# 1*1*1+2*2*2+3*3*3=1+8+27=36
# digit=123%10
# 3**3
num=int(input('enter the number'))
res=0

while(num>0):
    digit=num%10
    res=res+digit**3
    num//=10
print(res)

