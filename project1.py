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

def get_maxscore(subject):
    max=0
    for i in scores:
        if i[subject]>max:
            max=i[subject]

    hm='name'
    for i in scores:
        if i[subject]== max:
            print(f'{i[hm]} has one of the highest {subject} scores of {i[subject]} points')

get_maxscore('math')

get_maxscore('english')

get_maxscore('pe')

#miguel stanphill rank

def miguel_stanphill_rank(subject):
    ms=scores[0]
    rank=0
    for i in scores:
        if i[subject]>ms[subject]:
            rank+=1
    
    print(f"Miguel Stanphill's {subject} score is ranked {rank+1} place in the school")

miguel_stanphill_rank('math')
miguel_stanphill_rank('english')
miguel_stanphill_rank('pe')

