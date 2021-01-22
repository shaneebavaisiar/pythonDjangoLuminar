# read file demo and display that content in file

f=open('demo','r')
word=[]
for lines in f:
    print(lines)
# ==========================================================

# read file and print words in list
# method:1
f=open('demo','r')
words=[]
for lines in f:
    a=lines.rstrip('\n').split(' ')
    words.append(a)
print(words)
lst=[]
for wrd in words:
    for w in wrd:
        lst.append(w)
print('first method:',lst)
# =============================================================================
# method:2

f=open('demo','r')
wor=[]
for lines in f:
    a=lines.rstrip('\n').split(' ')
    for w in a:
        wor.append(w)
print('second method:',wor)

