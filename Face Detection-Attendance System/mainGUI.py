from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from studentGUI import Student_Management_System
from faceRecogniton import Face_Detector
import cv2
import tkinter.messagebox as tmsg
from tkinter import filedialog
import os

# root = Tk()
# root.geometry("1366x768")
# root.title("Face Recognition System")

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")
        
        
        title_label = Label(root, text="Face Recognition System", font="comicsansms 16 bold",pady=40)
        title_label.pack()

        b1 = Button(self.root, text="Student details",command=self.student_details, font="comicsansms 10 bold",relief=SOLID)
        b1.place(x=200,y=200,width=150,height=100)

        b2 = Button(root, text="Face Detector", command=self.face_detector, font="comicsansms 10 bold", relief=SOLID)
        b2.place(x=450, y=200, width=150, height=100)

        b3 = Button(root, text="Attendance",command=self.showattendance, font="comicsansms 10 bold", relief=SOLID)
        b3.place(x=700, y=200, width=150, height=100)

        b4 = Button(root, text="Help Desk",command=self.helpdeskinfo, font="comicsansms 10 bold", relief=SOLID)
        b4.place(x=950, y=200, width=150, height=100)

        b5 = Button(root, text="Train Data", font="comicsansms 10 bold", relief=SOLID)
        b5.place(x=200, y=400, width=150, height=100)

        b6 = Button(root, text="Photos", font="comicsansms 10 bold", relief=SOLID)
        b6.place(x=450, y=400, width=150, height=100)

        b7 = Button(root, text="Developer",command=self.dev_name, font="comicsansms 10 bold", relief=SOLID)
        b7.place(x=700, y=400, width=150, height=100)

        b8 = Button(root, text="Exit", font="comicsansms 10 bold", relief=SOLID, command=quit)
        b8.place(x=950, y=400, width=150, height=100)


#====Function Buttons ========

    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Student_Management_System(self.new_window)

    def face_detector(self):
        Face_Detector(root)
        
    def dev_name(self):
        tmsg.showinfo("Developers", "Developed by Group 2\n\nJayesh\nMihir\nDadasaheb\n\n**THANK YOU FOR USING OUR PROGRAM!!**")

    def helpdeskinfo(self):
        tmsg.showinfo("Help", "1)Student Details - Enter Student Details\n\n2)Face Detector - Attendace Start\n\n3)Attendace - Open Attendace List\n\n**This Program is under development**")

    def showattendance(self):
        open_attendance = filedialog.askopenfilename()
        os.system('"%s"' % open_attendance)





# root.mainloop()
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()