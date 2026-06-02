import os

units=["B" ,"KB", "MB", "GB", "TB"]

def convertBytes(size):
    if size==0:
        return "0 B"
    
    i=0

    while size>=1024 and i<len(units)-1:
        size/=1024
        i+=1

    return f"{size:.2f} {units[i]}"

#number of files and folders, total size

def basicInfo(path):
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

def sortSize(path):
    array=[]

    for root, dirs, files in os.walk(path):
        for i in files:
            p=os.path.join(root, i)
            s=os.path.getsize(p)
            array.append((p, s))

    array.sort(key=lambda x:x[1], reverse=True)
    print(array)

#converting bytes to kb,mb,gb,etc.

def formatSize(path):
    array=[]

    for root, dirs, files in os.walk(path):
        for i in files:
            p=os.path.join(root, i) 
            s=os.path.getsize(p)
            array.append((p, s))

    array.sort(key=lambda x:x[1], reverse=True)

    for p, s in array:
        print(f"{convertBytes(s):>20}  {p}")

#File type count

def fileTypeCount(path):
    dic={}

    for root, dirs, files in os.walk(path):
        for i in files:
            type=os.path.splitext(i)[1]
            if type=="":
                type="[No extension]"
            if type in dic:
                dic[type]+=1
            else:
                dic[type]=1

    dic=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

    print("\nFile Types:\n")

    for extension, count in dic.items():
        print(f"{extension:<15} {count}")

#analyze folder

def analyzeFolder(path):
    basicInfo(path)
    sortSize(path)
    formatSize(path)
    fileTypeCount(path)

#main

path=str(input("Enter absolute path of the folder: "))
analyzeFolder(path)

