# Note: You can only remove empty folders.


import os

try:
    os.rmdir('file-handling-files')
except OSError:
    print('Directory is not empty.You can only remove empty folders.')
