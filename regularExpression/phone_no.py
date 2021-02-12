from re import *
phone_no=input('enter phone number')

rule="(91)?\d{10}"
matcher =fullmatch(rule,phone_no)
if matcher==None:
    print('invalid phone  number')
else:
    print('valid phone number')