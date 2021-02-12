from functools import reduce

lst=[10,11,12,13,14]
sum=reduce(lambda num1,num2:num1+num2,lst)
print(sum)
# find heighest number from the list
high=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(high)

# find smallest number from the list
high=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(high)

# [1,2,3,4] [2,4,5,6,8] find common number in an efficient manner