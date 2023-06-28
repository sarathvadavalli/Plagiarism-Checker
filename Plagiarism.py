import os
import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher
F = []

root = tk.Tk()
root.title("Plagiarism checker")
root.configure(background="light green")
root.geometry('650x350')
root.resizable('FALSE','FALSE')

title = tk.Label(root, text = 'Plagiarism Checker', fg = 'red', bg = 'light blue', font = ('bold',15))
title.place(x = 230,y = 1)

def AskFile1():
    path = filedialog.askopenfile()
    if path:
        f1 = path.name
        F.append(f1)
        tk.Label(root, text = f1).place(x = 210,y = 62)
   
def AskFile2():
    path = filedialog.askopenfile()
    if path:
        f2 = path.name 
        F.append(f2)
        tk.Label(root, text = f2).place(x = 210,y = 126)
    
def Check():
    with open(F[0]) as first_file, open(F[1]) as second_file:
        file1 = first_file.read()
        file2 = second_file.read()

    ab = SequenceMatcher(None, file1, file2).ratio()
    result = int(ab*100)
    res['text'] = f"The plagiarised content is:\n\n{str(result)}%"
    print("Plagiarised content: "+str(result)+"%")

btn1 = tk.Button(root, text = 'Choose File1', bg = 'brown', fg = 'white', command = AskFile1)
btn1.place(x = 130,y = 60)
btn2 = tk.Button(root, text = 'Choose File2', bg = 'brown', fg = 'white', command = AskFile2)
btn2.place(x = 130,y = 124)

btn = tk.Button(root, text = 'Check Plagiarism',bg = 'orange',font = ('bold',10), command = Check)
btn.place(x = 230,y = 184)
res = tk.Label(root, width = 30, font = ('bold',12), bg = 'pink', fg = 'blue')
res.place(x = 170,y = 250)

root.mainloop()