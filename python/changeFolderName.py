import os
import re

dirs = os.listdir(os.curdir)
i = 0
for dir in dirs:
    # if dir is a folder
    if os.path.isdir(dir) == True: 
        os.rename(str(dir),str(i))
        i += 1

    # if dir is a file
    # if os.path.isfile(dir) == True:

#print(dirs)
