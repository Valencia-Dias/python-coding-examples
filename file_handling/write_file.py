with open('file-handling-files/abc.txt', 'w') as f:
    f.write('Writing to a file')
    f.close()

#After writing, open and read the same file
# Note: Unlike open() where you have to close the file with
#     the close() method, the with statement closes the file for you without you telling it to.
f = open('file-handling-files/abc.txt')
print(f.read())








# Multiple ways of creating a file


f = open('file-handling-files/2.txt', 'x')

f1 = open('file-handling-files/1.txt', 'x')
with open('file-handling-files/3.txt', 'x') as f3:
    pass
