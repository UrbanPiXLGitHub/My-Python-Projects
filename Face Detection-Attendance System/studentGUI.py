from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")



        # root = Tk()
        # root.geometry("1366x768")
        # root.title("Face Recognition System")

        title_label = Label(root, text="Student Management System", font="comicsansms 16 bold",pady=5)
        title_label.pack()

        main_frame = Frame(root,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #Left Label Frame

        Left_Frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_Frame.place(x=10, y=10,width=660, height=580)

        #Current Course Information

        Current_Course_Frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        Current_Course_Frame.place(x=20,y=75,width=645, height=200)

        dep_label= Label(Current_Course_Frame, bd=2,bg="white", relief=RIDGE, text="Department", font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,sticky=W,pady=10,padx=10)

        dep_combo = ttk.Combobox(Current_Course_Frame, font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CS","IT","Instrumentation","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,sticky=W,pady=10,padx=10)

        dep_label= Label(Current_Course_Frame, bd=2,bg="white", relief=RIDGE, text="Course", font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=2,sticky=W,pady=10,padx=10)

        dep_combo = ttk.Combobox(Current_Course_Frame, font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("FE","SE","TE","BE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,sticky=W,pady=10,padx=10)

        dep_label= Label(Current_Course_Frame, bd=2,bg="white", relief=RIDGE, text="Year", font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=0,sticky=W,pady=10,padx=10)

        dep_combo = ttk.Combobox(Current_Course_Frame, font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("2020-21","2021-2022","2022-23","2023-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,sticky=W,pady=10,padx=10)

        dep_label= Label(Current_Course_Frame, bd=2,bg="white", relief=RIDGE, text="Semester", font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=2,sticky=W,pady=10,padx=10)

        dep_combo = ttk.Combobox(Current_Course_Frame, font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("1st","2nd")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,sticky=W,pady=10,padx=10)

        #Class Student Information

        Class_Student_Frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        Class_Student_Frame.place(x=20,y=260,width=645, height=320)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="Student ID: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=0,column=0,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=0,column=1,padx = 10,sticky=W,pady=10)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="Student Name: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=0,column=2,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=0,column=3,padx = 10,sticky=W,pady=10)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="Class: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=1,column=0,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=1,column=1,padx = 10,sticky=W,pady=10)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="Division: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=1,column=2,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=1,column=3,padx = 10,sticky=W,pady=10)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="Roll.No.: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=2,column=0,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=2,column=1,padx = 10,sticky=W,pady=10)

        Student_Id_label= Label(Class_Student_Frame, bd=2,bg="white", relief=RIDGE, text="DOB: ", font=("times new roman",12,"bold"))
        Student_Id_label.grid(row=2,column=2,sticky=W,pady=10)

        StudentID_Entry = ttk.Entry(Class_Student_Frame, width=20, font=("times new roman",12,"bold"))
        StudentID_Entry.grid(row=2,column=3,padx = 10,sticky=W,pady=10)

        #Radio Buttons

        radiobtn1 = ttk.Radiobutton(Class_Student_Frame, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(Class_Student_Frame, text="No Sample", value="No")
        radiobtn2.grid(row=6,column=1)

        #Buttons Frame

        btn_frame =  Frame(Class_Student_Frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=180, width=640, height=100)

        save_btn=Button(btn_frame,text="Save",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        update_photo_btn.grid(row=1,column=1)



        #Right Label Frame

        Right_Frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_Frame.place(x=680, y=10,width=660, height=580)   
        
        right_frame_title = Label(Right_Frame, text="Enter Student Details",bg="white", font=("times new roman",24,"bold"))
        right_frame_title.pack()

        # ====Search System====4


if __name__ == "__main__":
    root=Tk()
    obj=Student_Management_System(root)
    root.mainloop()

# root.mainloop() 