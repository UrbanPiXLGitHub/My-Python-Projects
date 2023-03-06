import tkinter as tk
import math
root = tk.Tk()
root.title("Calculator1")
expression = " "
def add(Value):
    global expression
    expression += Value
    label_result.config(text=expression)
def clear():
    global expression
    expression = " "
    label_result.config(text=expression)

def calculate():
    global expression
    result = eval(expression)
    label_result.config(text=result)
    expression = str(result)

label_result = tk.Label(root , text = " ",width=16)
label_result.grid(row = 0 , column = 0,columnspan=4)
button_1 = tk.Button(root, text = "1",command= lambda: add("1"))
button_1.grid(row=1,column=0)
button_2 = tk.Button(root, text = "2",command= lambda: add("2"))
button_2.grid(row=1,column=1)
button_3 = tk.Button(root, text = "3",command= lambda: add("3"))
button_3.grid(row=1,column=2)
button_plus = tk.Button(root, text = "+",command= lambda: add("+"))
button_plus.grid(row=1,column=3)
button_4 = tk.Button(root, text = "4",command= lambda: add("4"))
button_4.grid(row=2,column=0)
button_5 = tk.Button(root, text = "5",command= lambda: add("5"))
button_5.grid(row=2,column=1)
button_6 = tk.Button(root, text = "6",command= lambda: add("6"))
button_6.grid(row=2,column=2)
button_minus = tk.Button(root, text = "-",command= lambda: add("-"))
button_minus.grid(row=2,column=3)
button_7 = tk.Button(root, text = "7",command= lambda: add("7"))
button_7.grid(row=3,column=0)
button_8 = tk.Button(root, text = "8",command= lambda: add("8"))
button_8.grid(row=3,column=1)
button_9 = tk.Button(root, text = "9",command= lambda: add("9"))
button_9.grid(row=3,column=2)
button_mul = tk.Button(root, text = "",command= lambda: add(""))
button_mul.grid(row=3,column=3)
button_C = tk.Button(root, text = "C",command= lambda: clear())
button_C.grid(row=4,column=0)
button_0 = tk.Button(root, text = "0",command= lambda: add("0"))
button_0.grid(row=4,column=1)
button_dot = tk.Button(root, text = ".",command= lambda: add("."))
button_dot.grid(row=4,column=2)
button_div = tk.Button(root, text = "/",command= lambda: add("/"))
button_div.grid(row=4,column=3)
button_eq = tk.Button(root, text = "=",width=16,command= lambda: calculate())
button_eq.grid(row=6,column=0,columnspan=4)

root.mainloop()