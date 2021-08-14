s1='helen'
s2=' h elen '
s3=s2.strip()
print(s3)

line='claire tang,99,98,87'
la=line.split(',')
print(la)

import matplotlib.pyplot as plt
numbers=[2,4,5,7,1,9]
plt.plot(numbers)
plt.show()

x=range(-50,50)
y=[i**2 for i in x]
plt.plot(x,y)
plt.xlabel('domain')
plt.ylabel('square(x)')
plt.show()
