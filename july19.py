from os import get_terminal_size


print('a good day')

print('helen')

name='helen'
print('hello '+ name)
print(f'hello {name}')

air='off'
temp=92
too_hot=temp>95
if too_hot:
    air='on'
    print('too hot')


temp=92
air=''
if temp>90:
    air='on'
else:
    air='off'
print(air)

temp=65
go_out= False
if temp>=50 and temp<70:
    go_out=True
    print('go out...')

age=12
school='GMS'
if age>11 and age<15:
    print('middle school')
elif age>20:
    print('college')

age=14
school='GMS'
if age>11 and age<15:
    print('middle school')
    if school in ['GMS','CMS']:
        print('WWP MS')
    else school in ['PUMS','Monty']:
        print('not WWP MS')
else:
    ('not MS')
