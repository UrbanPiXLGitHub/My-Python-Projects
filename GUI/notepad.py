from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def NewFile():
    global file
    root.title("Untitled - NotePad")
    file = None
    textbox.delete(1.0, END)


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files","*.*"), ("Text Documents","*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - NotePad")
        textbox.delete(1.0, END)
        f = open(file, "r")
        textbox.insert(1.0, f.read())
        f.close()

def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                           ("All Files","*.*"), ("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, "w")    
            f.write(textbox.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + " - NotePad")
    
    else:
        f = open(file, "w")    
        f.write(textbox.get(1.0, END))
        f.close()    

def QuitApp():
    root.destroy()


def cut():
    textbox.event_generate(("<<Cut>>"))


def copy():
    textbox.event_generate(("<<Copy>>"))


def paste():
    textbox.event_generate(("<<Paste>>"))


def About():
    showinfo("About", "This is a NotePad by Jayesh")


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x700")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("C:\\Users\\HP INDIA\\Downloads\\MyCustomIcon1.ico")

    # Creating Text Area
    textbox = Text(root, font="lucida 14")
    textbox.pack(expand=TRUE, fill=BOTH)
    file = None

    # Menubar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New File", command=NewFile)

    # To open an already existing file
    FileMenu.add_command(label="Open", command=OpenFile)

    # To save file
    FileMenu.add_command(label="Save", command=SaveFile)

    # To exit
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=QuitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpBar = Menu(MenuBar, tearoff=0)
    HelpBar.add_command(label="About Notepad", command=About)
    MenuBar.add_cascade(label="About", menu=HelpBar)

    root.config(menu=MenuBar)

    scroll = Scrollbar(textbox)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textbox.yview)
    textbox.config(yscrollcommand=scroll.set)

    root.mainloop()
