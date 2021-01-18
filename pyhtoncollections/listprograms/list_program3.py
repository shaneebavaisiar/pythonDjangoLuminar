lst=[10,11,12,13,14,15,16,17]
evnlist=[]
oddlist=[]
for num in lst:
    if num%2==0:
       evnlist.append(num)
    else:
        oddlist.append(num)
print('even',evnlist)
print('odd',oddlist)
print('sumevn',sum(evnlist))
print('sumodd',sum(oddlist))