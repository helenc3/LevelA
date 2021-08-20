def import_data():
    filename='google_stk.csv'
    with open(filename,mode='r') as handler:
        lines=(line for line in handler)
        skip=next(lines)
        records=[]
        for line in lines:
            values=line.strip().split(',')
            records.append(float(values[1]))
    records.reverse()
    return records

def compute_increase(records):
    index=1
    la=[]
    days=0
    while index<len(records)-1:
        if records[index-1]<records[index]:
            days+=1
            index+=1
        else:
            la.append(days)
            days=0
            index+=1      

    increase={}
    for i in range(1,16):
        increase.update({i:la.count(i)})

    return increase

def compute_decrease(records):
    index=1
    la=[]
    days=0
    while index<len(records)-1:
        if records[index-1]>records[index]:
            days+=1
            index+=1
        else:
            la.append(days)
            days=0
            index+=1      

    decrease={}
    for i in range(1,16):
        decrease.update({i:la.count(i)})
    return decrease

records=import_data()
increase=compute_increase(records)
decrease=compute_decrease(records)

print(increase)
print(decrease)









