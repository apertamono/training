import os
import random

# My first python program
# Create a list of image files in multiple directories and subdirectories
# Shuffle the list randomly before you print it to a text file
# Paths are defined for Windows
# Tested in Python 3.5.2 and 3.6.4
# Could the condition in line 18 be more compact?

path = 'C:\\Data\\Images\\Memes\\'

files = []
def listfunction():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file or '.png' in file or '.gif' in file or '.jpeg' in file:
                files.append(os.path.join(r, file))

listfunction()

path = 'C:\\Data\\Images\\Cringe\\'
listfunction()
        
random.shuffle(files)
for f in files:
    print(f)
