from os import name


la=[]
filename = 'testscores.csv'
handler = open(filename, mode='r')
content = handler.readlines()
for line in content:
	la.append(line.split(','))
handler.close()

names=[]
for x in la:
    names.append(x[0])

unique_names = set(names)
for n in unique_names:
    if names.count(n) > 1:
        print(n)


print(len(names))
print(len(unique_names))