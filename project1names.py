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

not_unique=[]
for name in names:
    x=name
    names.remove(name)
    for oname in names:
        if name==oname:
            not_unique.append(name)
            names.remove(oname)

if len(not_unique)>=2:
    print(f'the names {not_unique} are shared between two or more students')
elif len(not_unique)==1:
    print(f'the name {not_unique} is shared between two or more students')
else:
    print('sorry, there are no common names among the students')
