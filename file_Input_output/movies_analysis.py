f=open('movies.csv','r')
dict={}
for lines in f:
    data=lines.rstrip('\n').split(',')
    movies=int(data[2])
    if(movies not in dict):
        dict[movies]=1
    else:
        dict[movies]+=1

# print(dict)
for k,v in dict.items():
    print(k,'==>',v)
sort=sorted(dict,key=dict.get,reverse=True)
print('maximum movies released in:',sort[0],'===>',dict.get(sort[0]))