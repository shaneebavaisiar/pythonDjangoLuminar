lst=[1,2,3,4,6]
sqlst=list(map(lambda num:num**2,lst))
print(sqlst)
a=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(a)