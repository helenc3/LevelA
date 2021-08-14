def print_factors(a):
    for i in range(1,a+1):
        if a % i ==0:
            print(i)

print_factors(100)

def factors(a):
    la=[]
    for i in range(1,a+1):
        if a%i==0:
            la.append(i)
    return la

la=factors(20)
print(la)

def welcome(school='GMS', student)
    print(f'{school} welcome {student}')

welcome('GMS', 'Claire')
welcome('CMS', 'Helen')