name='helen'
name1= name.capitalize()
print(name1)

title='GREATWALL'
title2=title.casefold()
print(title2)
name='Helen'
name.count('e')

fname='string.py'
x=fname.endwith('.py')
print(x)

s1='238'
s2='ww2'
s1.isnumeric()
s2.isnumeric()

a=''
while not a.isnumeric():
    print('please input a number:')
    a=input()

name=' helen '
name =='helen'
name1=name.strip()
print(name1)

line='helen, 90, 89, 70'
la=line.split(',')
print(la)
name=la[0]
math=int(la[1].strip())
print(name)
print(math)

today='8-3-2021'
la=today.split('-')
month=int(la[0])
date=int(la[1])
year=int(la[2])
print(month+date+year)

la=['helen','claire','nancy']
','.join(la)
