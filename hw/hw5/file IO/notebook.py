import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def openFile(): 
    global filePath
    
    filePath = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files","*.*"),
                                      ("Text Documents","*.txt")]) 
    if filePath == "":         
        # no file to open 
        filePath = None
    else:         
        # Try to open the file 
        # set the window title 
        root.title(os.path.basename(filePath) + " - Notepad") 
        TextArea.delete(1.0,END) 

        file = open(filePath,"r") 

        TextArea.insert(1.0,file.read()) 

        file.close() 

## Main #############################################

root = Tk() 

# default window width and height 
Width = 300
Height = 300
TextArea = Text(root) 
MenuBar = Menu(root) 
FileMenu = Menu(MenuBar, tearoff=0) 
EditMenu = Menu(MenuBar, tearoff=0) 

# To add scrollbar 
ScrollBar = Scrollbar(TextArea)	 
filePath = None

# Set the window text 
root.title("Untitled - Notepad") 

# Center the window 
screenWidth = root.winfo_screenwidth() 
screenHeight = root.winfo_screenheight() 

# For left-alling 
left = (screenWidth / 2) - (Width / 2) 

# For right-allign 
top = (screenHeight / 2) - (Height /2) 

# For top and bottom 
root.geometry('%dx%d+%d+%d' % (Width, Height, left, top)) 

# To make the textarea auto resizable 
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1) 

# Add controls (widget) 
TextArea.grid(sticky = N + E + S + W) 

# To open a already existing file 
FileMenu.add_command(label="Open", command = openFile) 

MenuBar.add_cascade(label="File", menu = FileMenu)	 

# To give a feature of cut 
EditMenu.add_command(label="Cut", command = lambda:TextArea.event_generate("<<Cut>>"))

# To give a feature of editing 
MenuBar.add_cascade(label="Edit", menu = EditMenu)	 

root.config(menu=MenuBar) 

ScrollBar.pack(side=RIGHT,fill=Y)					 

# Scrollbar will adjust automatically according to the content		 
ScrollBar.config(command=TextArea.yview)	 
TextArea.config(yscrollcommand=ScrollBar.set) 

root.mainloop() 
