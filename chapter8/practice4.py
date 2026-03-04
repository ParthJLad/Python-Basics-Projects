# Print hpw many lines in the note.txt

import os
with open("note.txt", "r") as f:
    readLines = f.readlines()
    print(len(readLines))


# Rename the file

os.rename("main.txt", "parth.txt")
os.remove("parth.txt")