import os
file = 'file-handling-files/2.txt'

try:
    os.remove(file)
except FileNotFoundError:
    print("The file does not exist")