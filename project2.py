la=[]
filename = 'testscores.csv'
handler = open(filename, mode='r')
content = handler.readlines()
for line in content:
	la.append(line.split(','))
handler.close()

scores=[]
for x in la:
    record={'name':x[0],'total':int(x[1].strip())+int(x[2].strip())+int(x[3].strip())}
    scores.append(record)

max=0
for i in scores:
    if i['total']>max:
        max=i['total']

hm='name'
z='total'
for i in scores:
    if i['total']== max:
        print(f'{i[hm]} has the highest total score of {i[z]} points')