from tkinter import *

root = Tk()
root.title("Window Resizer")
root.geometry("600x400")

def resize():
    root.geometry(f"{heightentry.get()}x{widthentry.get()}")

widthtxt = Label(root, text="Width: ")
widthtxt.grid(row=0,column=0, padx= 10, pady=5)
heighttxt = Label(root, text="Height: ")
heighttxt.grid(row=1,column=0, padx= 10, pady=5)

height = StringVar()
width = StringVar()

heightentry = Entry(root, textvariable=height)
heightentry.grid(row=0, column=1, padx= 10, pady=5)
widthentry = Entry(root, textvariable=width)
widthentry.grid(row=1, column=1, padx= 10, pady=5)
Button(root, text="Resize", command= resize).grid(row=2, column=1, pady=5)

root.mainloop()