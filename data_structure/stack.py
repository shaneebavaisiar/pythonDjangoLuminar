size=int(input('enter the size of the stack'))
top=0
stack=[]
n=1

def push():
    item=int(input('enter the item'))
    global top
    if(top<size):
        stack.insert(top,item)
        top+=1
    else:
        print('stack overflow')

def pop():
    global top
    top-=1
    if top<0:
        print('stack is empty')
    else:
        print(stack[top],'popped out')
def display():
    for i in range(0,top):
        print(stack[i])
while(n!=0):
    option=int(input('enter operation press 1)push 2)pop 3)display'))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    n = int(input("if you want to continue press 0 for quit"))