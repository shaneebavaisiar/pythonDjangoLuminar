# print height repeating word frm the file demo
f=open('demo','r')
dict={}
for lines in f:
    words=lines.rstrip('\n').split(' ')
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)
sort=sorted(dict,key=dict.get,reverse=True)
print('morst repeated word is :',sort[0])
