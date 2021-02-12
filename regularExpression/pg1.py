# a,k first character must be a alphabet b/w a-k
# second must be a digit divisible by 3
# followed by any number of character



from re import *
variable_name=input('enter variable name')

rule="[a-k][369][a-zA-z0-9]*"
matcher =fullmatch(rule,variable_name)
if matcher==None:
    print('invalid variable')
else:
    print('valid variable')