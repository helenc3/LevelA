filename= 'note_text'
handler= open(filename, mode='r')
content= handler.read()
print(content)
handler.close()

filename= 'note_text'
handler= open(filename, mode='r')
content= handler.readlines()
print(content)
handler.close()

filename= 'note_text'
handler= open(filename, mode='r')
for line in handler:
   print(line) 
handler.close()