num1=int(input())
num2=int(input())
try:
    res=num1/num2
    print('res',res)
except Exception as e:
    print('exception occured')
print('i have one database transaction')
print('i have file operation')