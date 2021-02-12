from re import *
f=open('phoneNumbers','r')
for phone_nos in f:
    rule = "(\+91)?(0091)?(91)?\d{10}"
    phone_no=phone_nos.rstrip('\n')
    matcher = fullmatch(rule, phone_no)
    if matcher == None:
        pass
    else:
        print(phone_no)