# regular expression
#  step1 import re module
from re import *
pattern='[\bha]' #check for either a or b
# pattern='[a-z]' # will check for lower case a to z
matcher=finditer(pattern,'abc@ _7ZK@C ha haha')
# print(matcher)

for match in matcher:
    print(match.start(),'===>',match.group())

