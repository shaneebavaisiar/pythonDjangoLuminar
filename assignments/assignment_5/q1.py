# input lst=[1,2,3,4,5]
# write program to find pair whose sum is 6(or sum value can take from users)
# ===============================================================================
length=int(input('enter the max length of list:'))
lst=[]
for i in range(0,length):
    a=int(input('enter the values:'))
    lst.append(a)
print('lst:',lst)
k=int(input('enter the sum value of pair:'))
for num in lst:
    for n in lst:
        if num==n or num+n!=k:
            continue
        elif num+n==k:
            # lst.remove(num)
            lst.remove(n)
            print('(',num,n,')')

# or(sir method)
# lst=[1,2,3,4,5]
# num=6
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if (lst[i]+lst[j]==num):
#             print(lst[i],lst[j])