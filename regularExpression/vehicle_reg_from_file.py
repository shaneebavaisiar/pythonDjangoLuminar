from re import *
f=open('vehicle_reg_no','r')
for vehicle in f:
    pattern='kl\d{2}[a-zA-Z]{2}\d{4}'
    veh=vehicle.rstrip('\n')
    matcher=fullmatch(pattern,veh)
    if matcher==None:
        pass
    else:
        print(veh)
