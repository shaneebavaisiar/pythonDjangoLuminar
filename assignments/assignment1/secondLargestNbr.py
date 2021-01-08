#find three number and find heighst number
#find second largest number 40?
#sort these three numbers 30 40 50?

# num1=int(input('enter num1'))
# num1=int(input('enter num2'))
# num1=int(input('enter num3'))
a=int(input('enter the num1'))
b=int(input('enter the num2'))
c=int(input('enter the num3'))
# if(((a>b)&(a<c))|((a<b)&(a>c))):
#     print(a,'is second largest number')
# elif (((b > a) & (b < c)) | ((b < a) & (b > c))):
#     print(b,'is second largest number')
# elif (((c > a) & (c < b)) | ((c < a) & (c > b))):
#     print(c,'is the second largest number')
#OR
if((b<a<c)|(c<a<b)):
    print(a,'is second largest number')
elif ((a<b<c)|(c<b<a)):
    print(b,'is second largest number')
elif ((a<c<b) | (b<c<a)):
    print(c,'is the second largest number')