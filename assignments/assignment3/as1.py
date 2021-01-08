# class:05,4 jan 2021
# assigmnet:1
# Q:find all prime number between lower and upper limit ?
# =============================================================

lower_limit=int(input('enter lower limit:'))
upper_limit=int(input('enter upper limit:'))
flag=0
if lower_limit==1:
    lower_limit+=1
for i in range(lower_limit,upper_limit+1):
    for j in range(2,i):
        if i%j==0:
            flag+=1
            break
        else:
            flag=0
    if flag==0:
        print(i,end=' ')
    # else:
    #     print(i,'is not prime')