from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)
    

def equals():
    global equation_text
    try:
        total= str(eval(equation_text))
        equation_label.set(total)
        equation_text = total  # Update equation_text to the result for further calculations 
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
        
    except ZeroDivisionError:
        equation_label.set(" arithmetic Error")
        equation_text = ""
        
    

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

window = Tk()
window.title("Calculator program")
window.geometry("500x500")


equation_label = StringVar()

equation_text=""

Label = Label(window, textvariable=equation_label, font=("Arial", 24), bg="white", fg="black", anchor="e",width=20, height=2)
Label.pack()

Frame = Frame(window)
Frame.pack()

button1 = Button(Frame, text="1", command=lambda: button_press(1),
                 font=("Arial", 18), width=5, height=2)


button1.grid(row=0, column=0)

button2 = Button(Frame, text="2", command=lambda: button_press(2),
                 font=("Arial", 18), width=5, height=2)


button2.grid(row=0, column=1)
button3 = Button(Frame, text="3", command=lambda: button_press(3),
                 font=("Arial", 18), width=5, height=2)


button3.grid(row=0, column=2)
button4 = Button(Frame, text="4", command=lambda: button_press(4),
                 font=("Arial", 18), width=5, height=2)


button4.grid(row=1, column=0)

button5 = Button(Frame, text="5", command=lambda: button_press(5),
                 font=("Arial", 18), width=5, height=2)


button5.grid(row=1, column=1)

button6 = Button(Frame, text="6", command=lambda: button_press(6),
                 font=("Arial", 18), width=5, height=2)
button6.grid(row=1, column=2)

button7 = Button(Frame, text="7", command=lambda: button_press(7),
                 font=("Arial", 18), width=5, height=2)
button7.grid(row=2, column=0)

button8 = Button(Frame, text="8", command=lambda: button_press(8),
                 font=("Arial", 18), width=5, height=2)
button8.grid(row=2, column=1)

button9 = Button(Frame, text="9", command=lambda: button_press(9),
                 font=("Arial", 18), width=5, height=2)
button9.grid(row=2, column=2)
button0 = Button(Frame, text="0", command=lambda: button_press(0),
                 font=("Arial", 18), width=5, height=2)

button0.grid(row=3, column=0)

plus = Button(Frame, text="+", command=lambda: button_press('+'),
                 font=("Arial", 18), width=5, height=2)
plus.grid(row=0, column=3)

minus = Button(Frame, text="-", command=lambda: button_press('-'),
                 font=("Arial", 18), width=5, height=2)
minus.grid(row=1, column=3)

multiply = Button(Frame, text="*", command=lambda: button_press('*'),
                    font=("Arial", 18), width=5, height=2)
multiply.grid(row=2, column=3)

divide = Button(Frame, text="/", command=lambda: button_press('/'),
                 font=("Arial", 18), width=5, height=2)
divide.grid(row=3, column=3)

equals_button = Button(Frame, text="=", command=equals,
                       font=("Arial", 18), width=5, height=2)
equals_button.grid(row=3, column=2)

decimal = Button(Frame, text=".", command=lambda: button_press('.'),
                 font=("Arial", 18), width=5, height=2)


decimal.grid(row=3, column=1)

clear = Button(window, text="clear", command=clear,
                 font=("Arial", 18), width=7, height=2)

clear.pack()









window.mainloop()