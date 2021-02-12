size=int(input('enter the size'))
rear=0
front=0

queue=[]
def insertion():
    global rear
    if rear>=size:
        print('queue is full!')
    else:
        item=int(input('enter the element'))
        queue.insert(rear,item)
        rear+=1
def deletion():
    global front
    if rear==front:
        print('queue is empty')
    else:
        delete=queue[front]
        print('deleted element is',delete)
        front+=1
def display():
    print(queue)

n=1
while n!=0:
    option=int(input('enter the operation 1)insertion 2)deletion 3)display'))
    if option==1:
        insertion()
    elif option==2:
        deletion()
    elif option==3:
        display()
    n=int(input('if you want to continue press 0 for quit'))