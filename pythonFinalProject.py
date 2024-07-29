from tkinter import * 
from tkinter import scrolledtext
import tkinter.scrolledtext as st
import tkinter as tk
from tkinter.ttk import *
import os

def createFile():
    fileName = fileNameEntry.get()
    text = fileTextEntry.get("1.0", tk.END)
    with open(fileName,  mode="w") as file:
        file.write(text)

def appendFile():
    fileName = fileNameEntry.get()
    text = fileTextEntry.get("1.0", tk.END)
    with open(fileName, mode="a") as file:
        file.write(text)

def readFile():
    fileName = fileNameEntry.get()
    try:
        with open(fileName, mode="r") as file:
            content = file.read()
        showEntry.configure(state="normal")
        showEntry.delete("1.0", tk.END)
        showEntry.insert(tk.INSERT, content)
        showEntry.configure(state="disabled")
    except FileNotFoundError:
        showEntry.configure(state="normal")
        showEntry.delete("1.0", tk.END)
        showEntry.configure(state="disabled")

def updateFile():
    fileName = fileNameEntry.get()
    searchText = searchTextEntry.get()
    updateText = updateTextEntry.get()

    with open(fileName, mode="r") as file:
        data = file.read()
        updatedData = data.replace(searchText, updateText)
    with open(fileName, mode="w") as file:
        file.write(updatedData)

def deleteFile():
    fileName = fileLabelEntry.get()
    os.remove(fileName)

root = Tk()
root.title("GUI CRUD")

fileNameLabel = Label(root, text="File name :")
fileNameLabel.grid(row=0, column=0, sticky=W)

fileNameEntry = Entry(root)
fileNameEntry.grid(row=0, column=1, sticky=W)

fileTextLabel = Label(root, text="Text :")
fileTextLabel.grid(row=1, column=0, sticky=W)

fileTextEntry = scrolledtext.ScrolledText(root, wrap= WORD, width= 40, height= 8)
fileTextEntry.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=W)
fileTextEntry.focus()

createButton = Button(root, text="Create", command=createFile)
createButton.grid(row=2, column=2, sticky=S)

appendButton = Button(root, text="Append", command=appendFile)
appendButton.grid(row=3, column=2, sticky=N)

showLabel = Label(root, text="Show :")
showLabel.grid(row=1, column=3, sticky=W)

showEntry = st.ScrolledText(root, width= 40, height= 8)
showEntry.grid(row=2, column=3, rowspan=2)
showEntry.configure(state="disabled")

readButton = Button(root, text="Read", command=readFile)
readButton.grid(row=2, column=4, rowspan=2)

searchTextLabel = Label(root, text="Search text :")
searchTextLabel.grid(row=4, column=0, sticky=W)

searchTextEntry = Entry(root)
searchTextEntry.grid(row=5, column=0, sticky=W)

updateTextLabel = Label(root, text="Update text :")
updateTextLabel.grid(row=4, column=1, sticky=W)

updateTextEntry = Entry(root)
updateTextEntry.grid(row=5, column=1, sticky=W)

updateButton = Button(root, text="Update", command=updateFile)
updateButton.grid(row=4, column=2, rowspan=2, sticky=S)

fileLabel = Label(root, text="File :")
fileLabel.grid(row=6, column=0, sticky=W)

fileLabelEntry = Entry(root)
fileLabelEntry.grid(row=7, column=0, sticky=W)

deleteButton = Button(root, text="Delete", command=deleteFile)
deleteButton.grid(row=7, column=1, sticky=W)

root.mainloop()

#finalprojectsub.kodingakademi@gmail.com