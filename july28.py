filename= 'mynewfile'
with open(filename, 'w') as handler:
    handler.write('hello, good wednesday\n')

filename= 'mynewfile'
la=['helen ','bob\n','claire\n' '\n']
with open(filename, 'w') as handler:
    handler.writelines(la)