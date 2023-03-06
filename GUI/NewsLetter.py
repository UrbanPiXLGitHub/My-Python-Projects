# we have to make an article using tkinter GUI

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("1200x600")
root.title("The Newspaper")

def myfunc1():
    print("Creacting New Project")    
    
def myfunc2():
    print("Saving")       

def myfunc3():
    print("Save As")   

def myfunc4():
    print("Printing")  
    
def helpmsg():
     tmsg.showinfo("Help Bot", "I will help you.")        

def rate():
    exp = tmsg.askquestion("Help Bot", "Was your experience good using this GUI?")
    if(exp=="yes"):
        msg = "Thanks! please rate us on AppStore!"
    else:
        msg = "What went wrong? please let us know, we will look into it."    
    
    tmsg.showinfo("Help Bot", msg)
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc1)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="New Project", command=myfunc1)
m1.add_command(label="Save", command=myfunc2)
m1.add_command(label="Save As", command=myfunc3)
m1.add_separator()
m1.add_command(label="Print", command=myfunc4)

m2 = Menu(yourmenubar, tearoff=0)
m2.add_command(label="Help", command=helpmsg)
m2.add_command(label="Rate Us", command=rate)

yourmenubar.add_cascade(label="File", menu=m1)
yourmenubar.add_cascade(label="Feedback", menu=m2)
yourmenubar.add_command(label="Exit", command=quit)
root.config(menu=yourmenubar)

canvas1width = 800
canvas1height = 1000

canvas1 = Canvas(root, width=canvas1width, height=canvas1height)
canvas1.grid(column=1)

canvas1.create_line(110, 0, 110, 1000)
canvas1.create_line(534, 0, 534, 1000)

# font names --> Cooper, Forte, Gill Sans, Goudy Stout, Harlow Solid, Impact
title0 = Label(canvas1, text="Title: ", font='Forte 30')
title0.grid(row=0, column=0)

title1 = Label(canvas1, text="Article 1", font='Cooper 30')
title1.grid(row=0, column=1)

pic1 = Image.open("D:\\VScodes\\Python\\Well in that case.jpeg")
# image.resize((width, height))
image1 = ImageTk.PhotoImage(pic1.resize((190, 200)))
photo1 = Label(canvas1, image=image1)
photo1.grid(row=1, column=1, padx=10)

newsdescription1 = Label(
    canvas1, text="This a big news!!\nThis is a well in the case!! Yes!! You heard that right!! A \"Well\" Inside a \"case\"!!\n big news indeed!!\n(pun intended??)\n\n\n\n\n\n")
newsdescription1.grid(row=2, column=1, padx=10, pady=1)

root.mainloop()

# Can use frame instead of canvas
#side = UP,DOWN,LEFT,RIGHT
#anchor = E(ast), W(est), N(orth), S(outh)