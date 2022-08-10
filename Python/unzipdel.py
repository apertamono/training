# Extract all files from all zip files in a folder, then delete those zip files

# Doesn't check whether the file with .zip extension is actually a ZIP archive.
# Doesn't check for collisions, will overwrite files with duplicate names when they're in the same destination folder.

import zipfile, os
from os import listdir
from os.path import isfile, join
# os.path is a separate module, not part of os
# Importing specific functions, so we don't need to use a prefix

# Unusual variable names (directoire, onlyfiles, rits) were chosen to avoid using reserved names.
# Not using runtime input, to avoid accidentally deleting archives that need to be saved.
# Concatenating path and filename with `join(directoire, o)` is necessary in order to edit a folder other than the one this script is saved in.

directoire = "C:/Users/Edwin/Test"
onlyfiles = [f for f in listdir(directoire) if isfile(join(directoire, f))]
for o in onlyfiles:
    if o.endswith(".zip"):
        rits = zipfile.ZipFile(join(directoire, o), 'r')
        rits.extractall(directoire)
        print(o)
        rits.close()
        os.remove(join(directoire, o))
