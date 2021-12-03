import os

def getfilename(filename):
    if filename.count(".")>=1:
        pos = filename.rindex(',')
        newfile=filename[:pos]
        ext=filename[pos+1]
    else:
        newfile=filename
        exit=""
    return newfile, exit


dirlist=os.listdir("./")
for dir in dirlist:
    if os.path.isdir(dir):
        print("directory",dir)
    else:
        filename,ext=getfilename(dir)
        print("file",filename,ext)

