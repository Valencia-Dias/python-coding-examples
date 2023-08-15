# Multiple ways of creating a file
try:
    f = open('file-handling-files/1.txt', 'x')
    f1 = open('file-handling-files/2.txt', 'x')
    with open('file-handling-files/3.txt', 'x'):
        pass
except FileExistsError:
    print("The file already exists.")

