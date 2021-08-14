sleeping=True
time=1
while sleeping:
    print('dont call me')
    time+=1
    if time==10:
        sleeping=False
   
sleeping=True
time=1
while time<10:
    print('dont call me')
    time+=1

sleeping=True
time=1
while sleeping:
    print('dont call me')
    time+=1
    if time==10:
        break

kids=['helen','claire','bob','nancy','mike']
for index,kid in enumerate(kids):
    if kid=='nancy':
        print(f'index of nancy is {index}')
        break

kids={'helen':'f','claire':'f','bob':'m','nancy':'f','mike':'m'}
for kid in kids:
    if kids[kid]=='f':
        print(kid)

kids={'helen':'f','claire':'f','bob':'m','nancy':'f','mike':'m'}
for kid in kids:
    if kids[kid]=='m':
        continue
    print(kid)

la=[3,4,8]
lb=[]
for x in la:
    lb.append(2*x)
print(lb)

lb=[x*2 for x in la]
print(lb)

lb=[]
for i in range(101):
    if i%2==0:
        lb.append(i)
print(lb)

lb=[i for i in range(101) if i%2==0]
print(lb)

mat=[[9,8,7],[2,4,6],[8,2,5]]
m2=[]
for row in mat:
    row2=[i*2 for i in row]
    m2.append(row2)
print(m2)

kids=['helen','claire','bob','mike']
sports=['swimming','volleyball','tennis','fencing']
for kid in kids:
    for sport in sports:
        print(f'{kid} is doing {sport}')

f=[f'{kid} is doing {sport}' for kid in kids for sport in sports]
print(f)


        


