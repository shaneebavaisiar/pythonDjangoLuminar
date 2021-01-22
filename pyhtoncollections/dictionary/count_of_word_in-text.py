# find word count
# text='hello hai hello hai hello'
# count of hello:3
# count of hai:2
# ================================================
text = 'hello hai hello hai hello'
words=text.split(' ')
print('convert text into list:',words)
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)