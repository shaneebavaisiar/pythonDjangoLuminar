# regular expression
#  step1 import re module
from re import *
pattern='ab'
matcher=finditer(pattern,'ababababbbbaaababab')
cnt=0
print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)
