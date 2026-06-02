import tkinter as tk
from tkinter import filedialog
import main

#initialize tk window

window=tk.Tk()
window.title("Folder analyzer")
window.geometry("500x400")

#functions

path=""
nfolders=0 
nfiles=0
size=0.0
sortedArray=[]
fileTypes={}

def selectFolder():
    global path
    path=filedialog.askdirectory()
    pathLabel.config(text=path)

def analyze():
    if path!="":
        global nfolders, nfiles, size, sortedArray, fileTypes
        nfolders, nfiles, size, sortedArray, fileTypes=main.analyzeFolder(path)
        sortedText="\n".join(f"{main.convertBytes(s)} {p}" for p,s in sortedArray)

        foldersLabel.config(text=f"Folders: {nfolders}")
        filesLabel.config(text=f"Files: {nfiles}")
        sizeLabel.config(text=f"Size: {size}")
        sortLabel.config(text=sortedText)
        typesLabel.config(text=f"Types: {fileTypes}")
    else:
        errorLabel.config(text="Select a folder!")

#UI

header=tk.Label(window, text="Folder analyzer")
header.pack()

browse=tk.Button(window, text="Browse", command=selectFolder)
browse.pack()

pathLabel=tk.Label(window, text="No folder selected")
pathLabel.pack()

button=tk.Button(window, text="Analyze folder", command=analyze)
button.pack()

errorLabel=tk.Label(window, text="")
errorLabel.pack()

foldersLabel=tk.Label(window, text="Folders: ")
foldersLabel.pack()
filesLabel=tk.Label(window, text="Files: ")
filesLabel.pack()
sizeLabel=tk.Label(window, text="Size: ")
sizeLabel.pack()
sortLabel=tk.Label(window, text="Sorted: ")
sortLabel.pack()
typesLabel=tk.Label(window, text="Types: ")
typesLabel.pack()

#start looping

window.mainloop()