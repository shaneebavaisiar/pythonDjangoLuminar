num=int(input('enter the number:'))
orginal_value=num
reverse=""
while(num>0):
    digit=num%10
    reverse=reverse+str(digit)
    num=num//10
reverse=int(reverse)
print('reverse of the numbr:',reverse)
if(reverse==orginal_value):
    print('it is palindrome')
else:
    print('not palindrome')