import os
import re

dirs = os.listdir(os.curdir)
i = 0
for dir in dirs:
    
    if os.path.isdir(dir) == True:
        os.rename(str(dir),str(i))
        i += 1

#print(dirs)
