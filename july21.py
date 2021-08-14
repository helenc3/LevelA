la=(3,5,11,2,8,4)
mx=la[0]
for x in la:
    if x>mx:
        mx=x
print(f'the max is {mx}')

la=(3,5,11,2,8,4)
sm=0
for i in la:
    sm+=i
print(f'the sum is {sm}')


la=(3,5,11,2,8,4)
lb=[]
for i in la:
    lb.append(i*2)
print(lb)

kids=['helen', 'claire', 'nancy', 'allison']
sports=['swim','fencing','skating','tennis','xc']
for kid in kids:
    for sport in sports:
        print(f'{kid} is doing {sport}')