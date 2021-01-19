lst=[1,2,3,4,5]
element=int(input('entr the element for search:'))
flag=0
for i in lst:
    if element==i:
        flag+=1
    else:
        pass
if flag==0:
    print('not found')
else:
    print('found')