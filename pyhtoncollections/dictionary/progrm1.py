expences={'jan20':30000,'feb20':20000,'march20':20000}
# add key
expences['april20']=25000
print(expences)
# to check feb20 is in expences
print('feb20' in expences)
# to change already value
expences['march20']-=5000
print(expences['march20'])