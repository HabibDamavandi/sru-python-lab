from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Hello tkinter!")
window.geometry('500x100')

v1 = StringVar()

def btnClick(event):        
    v1.set(event.widget['text'])
    if (event.widget['text']=="Exit"):
        messagebox.showwarning("Warning","bye bye!")
        window.destroy()

lbl1 = Label(window, text="Button:", font=('Helvetica', 18, 'bold'))
lbl1.grid(column=0, row=0 ,sticky=W)

txt1 = Entry(window, width=20, textvariable = v1, font=('Helvetica', 18, 'bold'))
txt1.grid(column=1, row=0, columnspan=2, padx=2)
    
btn1 = Button(window, text="Hello GUI!", width=10, fg="red", font=('Helvetica', 18, 'bold'))
btn1.grid(column=1, row=1, padx=2, pady=5)
btn1.bind('<Button-1>', btnClick)

btn2 = Button(window, text="Exit", width=10, fg="red", font=('Helvetica', 18, 'bold'))
btn2.grid(column=2, row=1, padx=2, pady=5)
btn2.bind('<Button-1>', btnClick)

window.mainloop()
