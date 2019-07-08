import os
import random

# My first python program
# Create a list of image files from multiple directories and subdirectories
# Shuffle the list randomly before you print it to a text file

# Limitations: 
# Paths are defined for Windows
# Tested in Python 3.5.2 and 3.6.4
# Instead of matching a substring, I should use pathlib or splitext
# Could the if-statement be more compact?
# Could the path be passed to a function?
# There were errors that stopped execution at filenames with Russian or Polish letters
# This code skips extensions in upper case, but I should run another script to change them to lower case anyway
# In production, print("  ", f) adds two spaces before every filename in order to log which images I used

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
