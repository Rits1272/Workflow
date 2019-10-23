import tkinter as tk 
from tkinter import filedialog, Text 
import os 
import sys

root = tk.Tk() 
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApps():
    filename = filedialog.askopenfilenames(initialdir='/home/friday', title='Select File', 
                                            filetypes=(('excetables','*.exe'), ('all files','*.*')))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()

def runApps():
    for app in apps:
       if sys.platform == 'win32':
           os.startfile(app)
       else:
           os.open(app)

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='#fff')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text='Open File', padx=10, 
                     pady=5, fg='#fff', bg='#263d42', command=addApps)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=10, 
                     pady=5, fg='#fff', bg='#263d42', command=runApps)
runApps.pack()

for app in apps:
    label = tk.label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',') 