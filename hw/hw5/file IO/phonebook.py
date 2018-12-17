from tkinter import *
########################################
def append_entry_fields():
    # open file for write data
    f = open("phone.txt", "a",  encoding="utf-8")
    textstr = "%s \t %s \t %s \n" % (s1.get(),s2.get(),s3.get())
    f.write(textstr)
    s1.set("");s2.set("");s3.set("")
    e1.focus_set()
    print(textstr)
    f.close()
    return
########################################   
master = Tk()
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
master.title("دفتر تلفن")
Label(master, text="نام").grid(row = 0, column=1, sticky = E)
Label(master, text="نام خانوادگي").grid(row = 1, column=1, sticky = E)
Label(master, text="شماره تلفن").grid(row = 2, column=1, sticky = E)
e1 = Entry(master, textvariable=s1, justify=RIGHT)
e2 = Entry(master, textvariable=s2, justify=RIGHT)
e3 = Entry(master, textvariable=s3, justify=RIGHT)
e1.grid(row = 0, column = 0, sticky = E)
e2.grid(row = 1, column = 0, sticky = E)
e3.grid(row = 2, column = 0, sticky = E)
button1 = Button(master, text = 'خروج', command = master.destroy)
button1.grid(row = 3, column = 0, sticky = W, pady = 4)
button2 = Button(master, text = 'پاک کردن', command = lambda:(s1.set(""),s2.set(""),s3.set("")))
button2.grid(row = 3, column = 0, sticky = E, pady = 4)
button3 = Button(master, text = 'افزودن به ليست', command = append_entry_fields)
button3.grid(row = 3, column = 1, sticky = E, pady = 4)
mainloop( )
 
