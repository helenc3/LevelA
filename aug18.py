def squaregena():
    i=1
    sq=i**2
    while True:
        yield sq
        i+=1
        sq=i**2

for x in squaregena():
    print(x)
    if x>1000:
        break

def fib():
    f2=1
    f1=0
    while True:
        f=f2+f1
        yield f
        f1=f2
        f2=f

for x in fib():
    if x<2000:
        print(x)