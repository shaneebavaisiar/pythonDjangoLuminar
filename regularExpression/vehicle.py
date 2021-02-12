# rule of vehicle registration
# validate vehicle regno
# kl 2digtwo 2alphabet 4 digit


from re import *
reg_no=input('enter registration number')

rule="kl\d{2}[A-Za-z]{2}\d{4}"
matcher =fullmatch(rule,reg_no)
if matcher==None:
    print('invalid registration number')
else:
    print('valid registration number')