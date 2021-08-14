la=[]
filename = 'testscores.csv'
handler = open(filename, mode='r')
content = handler.readlines()
for line in content:
	la.append(line.split(','))
handler.close()

scores=[]
for x in la:
    record={'name':x[0],
            'math':int(x[1].strip()),
            'english':int(x[2].strip()),
            'pe':int(x[3].strip()),
            }
    scores.append(record)

in_50_70=0
in_70_90=0
in_90_100=0

for i in scores:
    if i['math']>=50 and i['math']<=70:
        in_50_70+=1
    elif i['math']>70 and i['math']<=90:
        in_70_90+=1
    else:
        in_90_100+=1

print(f'{in_50_70} kids have a math score between 50 and 70 points')
print(f'{in_70_90} kids have a math score between 70 and 90 points')
print(f'{in_90_100} kids have a math score between 90 and 100 points')

