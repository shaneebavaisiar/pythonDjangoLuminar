employees=[
    [10,'christy','dataanalyst',50000],
    [11,'jhon','ba',30000],
    [12,'sab','dataanalyst',40000],
    [13,'tom','developer',40000],
    [14,'jhoni','developer',30000],
    [15,'sabir','dataanalyst',50000],
    [16,'tino','developer',40000],
    [17,'tomis','developer',47000],
    [18,'jhonis','developer',32000],
]
# # print number of employees in this company
# number_of_employees=len(employees)
# print('number of employees:',number_of_employees)
# # =========================================================
# # total amount in a company for one month
# total_amout=0
# for emp in employees:
#     total_amout+=emp[3]
# print('total amount:',total_amout)
# # ===============================================================
# # group by designation
#
# d_count,da_count,ba_count=0,0,0
# for emp in employees:
#     if emp[2]=='dataanalyst':
#         da_count+=1
#     elif emp[2]=='developer':
#         d_count+=1
#     else:
#         ba_count+=1
# print('developer count:',d_count)
# print('dataanalyst count:',da_count)
# print('ba count:',ba_count)
# # =================================================================
# # print highst salaried employee
# salaries_list=[]
# for emp in employees:
#     salaries_list.append(emp[3])
# hig_slary=max(salaries_list)
# print("heighst salary",hig_slary)
#
# for emp in employees:
#     if emp[3]==hig_slary:
#         print(emp[1])

# print employee name who recieves lowest salary Whose designation is developer
developer_salaries=[]
for emp in employees:
    if emp[2]=='developer':
        developer_salaries.append(emp[3])
print('devolepr salaries list:',developer_salaries)
dev_min_salaries=min(developer_salaries)
for emp in employees:
    if (emp[3]==dev_min_salaries) &(emp[2]=='developer'):
        print('developer name salary who got  minimum salary:',emp[1])
