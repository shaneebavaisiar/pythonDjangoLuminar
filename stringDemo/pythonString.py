# #how to represent string in python
#
# name='luminar technolab training'
# words=name.split(' ') #spliting string
# print(words)
# print(name.upper()) # conert spring to upper case
# print(name.lower()) #convert spring to lower case

# remove character from begining
name1='LuminarTechnolab'
words =name1.lstrip('L')
print(words)
#removing character from end
name2='shaneeba'
print('name:',name2.rsplit('a'))