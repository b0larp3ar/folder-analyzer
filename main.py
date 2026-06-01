import os

units=["B" ,"KB", "MB", "GB", "TB"]

def formatSize(size):
    if size==0:
        return "0 B"
    
    i=0

    while size>=1024 and i<len(units)-1:
        size/=1024
        i+=1

    return f"{size:.2f} {units[i]}"

def analyzeFolder(path):

    #number of files and folders, total size

    nfolders = 0
    nfiles = 0
    size=0

    for root, dirs, files in os.walk(path):
        nfolders=nfolders+len(dirs)
        nfiles=nfiles+len(files)
        for i in files:
            p=os.path.join(root, i)
            size=size+os.path.getsize(p)

    print(f"Number of folders: {nfolders}")
    print(f"Number of files: {nfiles}")
    print(f"Total size: {size}")

    #sorting based on file size

    array=[]

    for root, dirs, files in os.walk(path):
        for i in files:
            p=os.path.join(root, i)
            s=os.path.getsize(p)
            array.append((p, s))

    array.sort(key=lambda x:x[1], reverse=True)
    print(array)

    #converting bytes to kb,mb,gb,etc.

    array=[]

    for root, dirs, files in os.walk(path):
        for i in files:
            p=os.path.join(root, i)
            s=os.path.getsize(p)
            array.append((p, s))

    array.sort(key=lambda x:x[1], reverse=True)

    for p, s in array:
        print(f"{formatSize(s):>20}  {p}")


path=str(input("Enter absolute path of the folder: "))
analyzeFolder(path)
