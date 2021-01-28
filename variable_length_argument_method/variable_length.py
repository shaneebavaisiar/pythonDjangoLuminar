def add(*args):
    return sum(args)

total=add(10,20,30,40,50)
print(total)
# ========================================================================
# to print args in one by one we use for loop
def add(*args):
    for num in args:
        print(num)

add(10,20,30,40,50)
# =================================

def print_data(**kwars):
    print(kwars)

print_data(name='ajay',workinglocation='kakanad',home='tirssur')