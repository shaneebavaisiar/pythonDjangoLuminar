students=[
    [10,'ajay','bca',250],
    [11,'vjay','bca',250],
    [12,'sibin','bca',220],
    [13,'dino','mca',220],
    [14,'tom','mca',180],
    [15,'jain','mca',250]
]
# print students nmaes whose total>240
for stud in students:
    if stud[3]>240:
        print(stud[1])
# print total sum of total
marks=0
for stud in students:
    marks+=stud[3]
print(marks)

# calculate total of bca

mtotal,btotal=0,0
for stud in students:
    if stud[2]=='bca':
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print('mca',mtotal)
print('bca',btotal)
