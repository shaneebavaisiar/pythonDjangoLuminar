# find give arry is rotation of another array
# [1,2,3,4,5,6] is rotation of [4,5,6,1,2,3]
# ====================================================
# lst=[1,2,3,4,5,6,7,8,9,10,11,12]
# rotation_lst=[7,8,9,10,11,12,1,2,3,4,5,6]
# len_of_lst=len(lst)//2
# print(len_of_lst)
# l=lst[len_of_lst:]+lst[:len_of_lst]
# if l==rotation_lst:
#     print('it is rotation')
# else:
#     print('not rotation')

def rotation(lst,rotation_lst):
    new_lst=lst[len(lst)//2:]+lst[:len(lst)//2]
    if new_lst==rotation_lst:
        print('rotation')
    else:
        print('not rotation')

rotation([1,2,3,4,5,6,7,8],[5,6,7,8,1,2,3,4])