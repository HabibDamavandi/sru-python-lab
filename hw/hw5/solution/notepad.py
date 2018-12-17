import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def quitApplication(): 
    root.destroy() 

def showAbout(): 
    showinfo("Notepad","Hello :)") 

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

def newFile():
    global filePath
    root.title("Untitled - Notepad") 
    filePath = None
    TextArea.delete(1.0,END) 

def saveFile():
    global filePath
    if filePath == None:        
        # Save as new file 
        saveAsFile()        
    else: 
        file = open(filePath,"w") 
        file.write(TextArea.get(1.0,END)) 
        file.close()
        
def saveAsFile():
    global filePath
      
    # Save as new file 
    filePath = asksaveasfilename(initialfile='Untitled.txt',
                             defaultextension=".txt",
                             filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")]) 

    if filePath != "":
        # Try to save the file 
        file = open(filePath,"w") 
        file.write(TextArea.get(1.0,END)) 
        file.close() 
        
        # Change the window title 
        root.title(os.path.basename(filePath) + " - Notepad") 

def cut(): 
    TextArea.event_generate("<<Cut>>") 

def copy(): 
    TextArea.event_generate("<<Copy>>") 

def paste(): 
    TextArea.event_generate("<<Paste>>") 

## Main #############################################

root = Tk() 

# default window width and height 
Width = 500
Height = 300
TextArea = Text(root) 
MenuBar = Menu(root) 
FileMenu = Menu(MenuBar, tearoff=0) 
EditMenu = Menu(MenuBar, tearoff=0) 
HelpMenu = Menu(MenuBar, tearoff=0) 

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

# To open new file 
FileMenu.add_command(label="New", command=newFile)	 

# To open a already existing file 
FileMenu.add_command(label="Open", command=openFile) 

# To save current file 
FileMenu.add_command(label="Save", command=saveFile)	 

# To save current file as new file
FileMenu.add_command(label="Save As...", command=saveAsFile)	 

# To create a line in the dialog		 
FileMenu.add_separator()										 
FileMenu.add_command(label="Exit", command=quitApplication) 
MenuBar.add_cascade(label="File", menu=FileMenu)	 

# To give a feature of cut 
EditMenu.add_command(label="Cut", command=cut)			 

# to give a feature of copy	 
EditMenu.add_command(label="Copy", command=copy)		 

# To give a feature of paste 
EditMenu.add_command(label="Paste", command=paste)		 

# To give a feature of editing 
MenuBar.add_cascade(label="Edit", menu=EditMenu)	 

# To create a feature of description of the notepad 
HelpMenu.add_command(label="About Notepad", command=showAbout) 
MenuBar.add_cascade(label="Help", menu=HelpMenu) 

root.config(menu=MenuBar) 

ScrollBar.pack(side=RIGHT,fill=Y)					 

# Scrollbar will adjust automatically according to the content		 
ScrollBar.config(command=TextArea.yview)	 
TextArea.config(yscrollcommand=ScrollBar.set) 

root.mainloop() 
