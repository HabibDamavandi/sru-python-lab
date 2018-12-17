from math import sqrt
from tkinter import *

def btnClick(event):
    global clearResult
    global canChangeOprator
    global opr
    global firstOprand
    global memory
    btnText = event.widget['text']
    displayText = textVar.get()
    if btnText == "C":
        displayText = "0";
        opr = "";
        clearResult = False
        textVar.set(displayText)
    elif btnText == "CE":
        displayText = "0"
        textVar.set(displayText)
    elif btnText == "M+":
        clearResult = True
        memory += float(displayText)
    elif btnText == "M-":
        clearResult = True
        memory -= float(displayText)
    elif btnText == "MS":
        clearResult = True
        memory = float(displayText)
    elif btnText == "MR":
        displayText = ("%0.10f"%memory).rstrip('0').rstrip('.')
        clearResult = True
        canChangeOprator = False
        textVar.set(displayText)
    elif btnText == "±":
        sign = displayText[0]
        if (sign == "-"):
            displayText = displayText[1:]
        elif (displayText != "0"):
            displayText = "-" + displayText
        textVar.set(displayText)
    elif btnText == "√":
        displayText = ("%0.10f"%(sqrt(float(displayText)))).rstrip('0').rstrip('.')
        clearResult = True
        canChangeOprator = False
        textVar.set(displayText)
    elif btnText == "x²":
        displayText = ("%0.10f"%(float(displayText)**2)).rstrip('0').rstrip('.')
        clearResult = True
        canChangeOprator = False
        textVar.set(displayText)
    elif btnText == "1/x":
        displayText = ("%0.10f"%(1.0/float(displayText))).rstrip('0').rstrip('.') 
        clearResult = True
        canChangeOprator = False
        textVar.set(displayText)
    elif btnText == "%":
        displayText = ("%0.10f"%(firstOprand * float(displayText)/100.0)).rstrip('0').rstrip('.')
        clearResult = True
        canChangeOprator = False
        textVar.set(displayText)
    elif btnText in ".0123456789":
        canChangeOprator = False
        if (btnText == ".") and ("." in displayText):
            return
        if (clearResult):
            displayText = "0"
            clearResult = False
        if (displayText == "0") and (btnText != "."):
            displayText = ""
        displayText += btnText
        textVar.set(displayText)
    elif btnText == "←":
        if clearResult:
            return
        if (displayText != "0") and (btnText == "←"):
            displayText = displayText[0:-1]
            if (displayText == "") or (displayText == "-"):
                displayText = "0"
        textVar.set(displayText)
    elif btnText in "+-*/=":
        newOpr = btnText
        if (canChangeOprator and newOpr != "="):
            opr = newOpr
            return
        if (opr == "+"):
            firstOprand += float(displayText)
        elif (opr == "-"):
            firstOprand -= float(displayText)
        elif (opr == "*"):
            firstOprand *= float(displayText)
        elif (opr == "/"):
            firstOprand /= float(displayText)
        elif (opr == ""):
            firstOprand = float(displayText)

        opr = "" if(newOpr == "=") else newOpr
        displayText = ("%0.10f"%firstOprand).rstrip('0').rstrip('.')
        clearResult = True
        canChangeOprator = True
        textVar.set(displayText)
    else:
        return

## Main #############################################

master = Tk()
master.title("Calculator")
master.resizable(height=False, width=False)
btnText = ["MR","M+","M-","MS","%","√","x²","1/x","CE","C","←","/","7",
           "8","9","*","4","5","6","-","1","2","3","+","±","0",".","="]
textVar = StringVar()
clearResult = False
canChangeOprator = False
opr = ""
firstOprand = 0.0
memory = 0.0
textVar.set("0")

e1 = Entry(master, textvariable = textVar,
           width=12, justify = RIGHT,
           state = "readonly", font=("arial",26,"bold"))
e1.grid(row = 0, column = 0, columnspan=4, sticky=W)

for i in range(4):
    for j in range(7):
        btn = Button(master, width=3, height=1,
                     text = btnText[j*4+i], font=("arial",18,"bold"))
        btn.grid(row=j+1, column=i, padx=2, pady=2)
        btn.bind('<ButtonRelease-1>', btnClick)
master.mainloop()

