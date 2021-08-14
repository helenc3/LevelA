la=[3,6,8]
for i in la:
    print(i)

la=[1,2,3,4,5,6,7]
for x in la:
    if x%2==0:
        print(x)

list(range(8))

GPA= {'helen':4.3,'claire':4.3,'nancy':4.1,'bob':3.5}
for x in GPA.keys():
    print(x)
for k,v in GPA.items():
    print(k,v)

la=['claire','nancy','helen']
for index,name in enumerate(la):
    print(f'the index of {name} is {index}')

a=12348
for i in range(1,a+1):
    if a%i==0:
        print(i)