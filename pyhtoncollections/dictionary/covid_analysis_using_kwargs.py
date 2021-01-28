# print_data(state='kerala',prop='confirmed')
# ===============================================================

f=open('covid_19_india.csv','r')
dict={}

for lines in f:
    data=lines.rstrip('\n').split(',')
    # print(data)
    state,confirmed,cured=data[3].rstrip('***'),data[8],data[6]
    if (state == "Telengana"):
        state = 'Telangana'
    if state not in dict:
        dict[state]={'state':state,'confirmed':confirmed,'cured':cured}
    else:
        dict[state] = {'state':state ,'confirmed':confirmed, 'cured': cured}
print(dict)
def print_data(**kwargs):
    # print(kwargs)
    state=kwargs['state']
    # print(state)
    if state in dict:
        print(dict[state]['state'])
        if 'prop' in kwargs:
            prop=kwargs['prop']
            print(dict[state][prop])
    else:
        print('state doesnot exist')

print_data(state='West Bengal',prop='confirmed')