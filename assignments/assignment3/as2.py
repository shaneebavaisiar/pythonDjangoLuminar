#Q:read a number=2
# read lower limit=4
# read upper limit=20
# 1**2=1(not print bcz not in btween 4 and 20),
# 2**2==4(print 2 bcz it is btwn 4 and 20),
# 3**2=9(print 3 bcz it btwn 4 and 20),etc...
# =============================================================
number=int(input('enter a number:'))
lower_limit=int(input('enter lower limit:'))
upper_limit=int(input('enter upper limit:'))
val=[]
for i in range(lower_limit,upper_limit+1):
    for j in range(1,upper_limit+1):
        if j**number==i:
            val.append(j)
if val==[]:
    print('no values found')
else:
    print(val)


