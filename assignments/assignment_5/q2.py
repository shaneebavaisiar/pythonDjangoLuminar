# lst=[2,6,4] o/p[10,6,8]
# lst=[3,4,5] o/p[9,8,7]
# =======================================================================
# lst=[3,4,5]
length=int(input('enter the length of list'))
lst=[]
for i in range(0,length):
    num=int(input('enter the value:'))
    lst.append(num)
print('input list:',lst)
total_sum=sum(lst)
k=[]
for i in lst:
    i=total_sum-i
    k.append(i)
print('output list:',k)