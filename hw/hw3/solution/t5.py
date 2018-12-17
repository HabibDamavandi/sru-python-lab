from tkinter import *
window = Tk()
window.title("Simple Calculator")
window.geometry('500x200')
v1 = StringVar(); v2 = StringVar(); v3 =StringVar()

def btnClick(event):
    if(event.widget['text'] == "+"):
        result = float(v1.get()) + float(v2.get())
    elif (event.widget['text'] == "-"):
        result = float(v1.get()) - float(v2.get())
    elif (event.widget['text'] == "*"):
        result = float(v1.get()) * float(v2.get())
    elif (event.widget['text'] == "/"):
        result = float(v1.get()) / float(v2.get())
        
    v3.set("%s %s %s = %s" % (v1.get(),event.widget['text'],v2.get(), result))

lbl1 = Label(window, text="First Number:", font=('Helvetica', 18, 'bold'))
lbl1.grid(column=0, row=0 ,sticky=W)
txt1 = Entry(window, width=20, textvariable = v1, font=('Helvetica', 18, 'bold'))
txt1.grid(column=1, row=0, columnspan=4, padx=2)

lbl2 = Label(window, text="Second Number:", font=('Helvetica', 18, 'bold'))
lbl2.grid(column=0, row=1, sticky=W)
txt2 = Entry(window, width=20,textvariable = v2, font=('Helvetica', 18, 'bold'))
txt2.grid(column=1, row=1, columnspan=4, padx=2)

lbl3 = Label(window, text="Result:", font=('Helvetica', 18, 'bold'))
lbl3.grid(column=0, row=2, sticky=W)
txt3 = Entry(window, width=20, textvariable = v3, font=('Helvetica', 18, 'bold'))
txt3.grid(column=1, row=2, columnspan=4, padx=2)

    
btn1 = Button(window, text="+",width=3, fg="red", font=('Helvetica', 18, 'bold'))
btn1.grid(column=1, row=3, padx=2, pady=5)
btn1.bind('<Button-1>', btnClick)

btn2 = Button(window, text="-",width=3, fg="red", font=('Helvetica', 18, 'bold'))
btn2.grid(column=2, row=3, padx=2, pady=5)
btn2.bind('<Button-1>', btnClick)

btn3 = Button(window, text="*",width=3, fg="red", font=('Helvetica', 18, 'bold'))
btn3.grid(column=3, row=3, padx=2, pady=5)
btn3.bind('<Button-1>', btnClick)

btn4 = Button(window, text="/",width=3, fg="red", font=('Helvetica', 18, 'bold'))
btn4.grid(column=4, row=3, padx=2, pady=5)
btn4.bind('<Button-1>', btnClick)

window.mainloop()
