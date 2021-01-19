# lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
# output=[10,20,21,22,51,52,53,54]
# =========================================================
lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
# numlist=[]
# for sublst in lst:
#     for n in sublst:
#         numlist.append(n)
# print(numlist)




# or (list comprehension method)

numlist=[num for sublist in lst for num in sublist]
print(numlist)