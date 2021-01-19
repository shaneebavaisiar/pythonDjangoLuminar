# input lst=[1,2,3,4,5]
# write program to find pair whose sum is 6(or sum value can take from users)
# ===============================================================================
# lst=[1,2,3,5]
lst=[1,23,12,2,3,5,8,3,10,11,4,6,0,4,2]
lst.sort()
low=0
upp=len(lst)-1
element=int(input('enter element:'))
k=[]
while(low<upp):
    total=lst[low]+lst[upp]
    if element==total:
        a=lst[low],lst[upp]
        if a not in k:
            k.append(a)
        low+=1
        continue
    elif element>total:
        low+=1
    elif element<total:
        upp-=1
print(k)
