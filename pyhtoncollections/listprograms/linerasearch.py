lst=[1,2,3,4,6]
element=4
flag=0
for i in lst:
    if element==i:
        flag+=1
        break
    else:
        pass
if flag==0:
    print('elemnt not found')
else:
    print(' found')
