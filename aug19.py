import time

t1=time.time()
print(t1)

t0=time.time()
la=[]
for x in range(1000000):
    la.append(x)
t2=time.time()
print(t2-t0)

time.sleep(5)

import datetime

t1=datetime.time(12,37,0)
print(t1)

lunch=datetime.time(10,40,00)

d1=datetime.date(2021,8,19)
print(d1)

d2=datetime.date.today()
print(d2)

d2.weekday()


today=datetime.date.today()
d3=today.toordinal()
print(d3)

print(datetime.datetime.now())
