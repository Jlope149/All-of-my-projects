import tkinter as tk
from tkinter import *
root = Tk()
root.title("Simple Calculator")

display = Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

def button_click(number):
    current = display.get()
    display.delete(0,END)
    display.insert(0,str(current) + str(number))

def button_clear():
    display.delete(0, END)

def button_add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    display.delete(0, END)


def button_sub():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    display.delete(0, END)

def button_mult():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    display.delete(0, END)

def button_div():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0,END)
    if math_operation == "addition":
        display.insert(0,f_num + float(second_number))
    elif math_operation == "subtraction":
        display.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        display.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        display.insert(0,f_num / float(second_number))



button_1 = Button(root, text="1",padx=22,pady=20,command=lambda: button_click(1))
button_1.grid(row=4, column=0)

button_2 = Button(root, text="2",padx=20,pady=20,command=lambda: button_click(2))
button_2.grid(row=4, column=1)

button_3 = Button(root, text="3",padx=20,pady=20,command=lambda: button_click(3))
button_3.grid(row=4, column=2)

button_4 = Button(root, text="4",padx=20,pady=20,command=lambda: button_click(4))
button_4.grid(row=3, column=0)

button_5 = Button(root, text="5",padx=20,pady=20,command=lambda: button_click(5))
button_5.grid(row=3, column=1)

button_6 = Button(root, text="6",padx=20,pady=20,command=lambda: button_click(6))
button_6.grid(row=3, column=2)

button_7 = Button(root, text="7",padx=20,pady=20,command=lambda: button_click(7))
button_7.grid(row=2, column=0)

button_8 = Button(root, text="8",padx=20,pady=20,command=lambda: button_click(8))
button_8.grid(row=2, column=1)

button_9 = Button(root, text="9",padx=20,pady=20,command=lambda: button_click(9))
button_9.grid(row=2, column=2)

button_0 = Button(root, text="0",padx=20,pady=20,command=lambda: button_click(0))
button_0.grid(row=5, column=1)

button_neg = Button(root, text="neg",padx=12,pady=20,command=lambda: button_click("-"))
button_neg.grid(row=1, column=1)

button_dec = Button(root, text=".",padx=22,pady=20,command=lambda: button_click("."))
button_dec.grid(row=5, column=2)


button_plus = Button(root, text="+", padx=20, pady=20, command=button_add)
button_plus.grid(row=4, column=4)

button_minus = Button(root, text="-", padx=20, pady=20, command=button_sub)
button_minus.grid(row=3, column=4)

button_multiply = Button(root, text="x", padx=20, pady=20, command=button_mult)
button_multiply.grid(row=2, column=4)

button_divide = Button(root, text="÷", padx=20, pady=20, command=button_div)
button_divide.grid(row=1, column=4)

button_clear_btn = Button(root, text="C", padx=19,pady=20, command=button_clear)
button_clear_btn.grid(row=1, column=0)

button_equals_btn = Button(root, text="=", padx=20,pady=20, command=button_equal)
button_equals_btn.grid(row=5, column=4)

root.mainloop()
