import mysql.connector
from datetime import *
import time

from course import CourseClass
from student import StudentClass
from result import ResultClass
from tkinter import *
from report import ReportClass

from PIL import Image,ImageTk,ImageDraw

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x800+0+0")
        self.root.title("Result Management System")
        self.root.config(bg="white")
        self.logo=ImageTk.PhotoImage(file="images/logo_p.png")

        #title
        title=Label(self.root,text="Student Result Management System",font=("goudy old style",20,'bold'),bg="#033054",image=self.logo,fg='white',compound=LEFT,padx=10).place(x=0,y=0,relwidth=1,height=50)
         #menu Frame
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=50,width=1340,height=80)
        #Buttons in Frame
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=80,y=5,width=190,height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15), bg="#0b5377", fg="white",
                            cursor="hand2",command=self.add_student).place(x=310, y=5, width=190, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15), bg="#0b5377", fg="white",
                            cursor="hand2",command=self.result).place(x=540, y=5, width=190, height=40)
        btn_view = Button(M_Frame, text="View Student Records", font=("goudy old style", 15), bg="#0b5377", fg="white",
                            cursor="hand2",command=self.report).place(x=760, y=5, width=190, height=40)
        #btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15), bg="#0b5377", fg="white",
         #                   cursor="hand2").place(x=895, y=5, width=190, height=40)
        #btn_exit= Button(M_Frame, text="Course", font=("goudy old style", 15), bg="#0b5377", fg="white",
         #                   cursor="hand2").place(x=1115, y=5, width=190, height=40)
        #content window
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((600,220),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=250,y=150,width=600,height=220)



        #update
        self.lbl_course=Label(self.root,text="Total Course\n[0]",font=("goudy old style", 15),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=250,y=400,width=200,height=70)
        self.lbl_student = Label(self.root, text="Total Student\n[0]", font=("goudy old style", 15), bd=10, relief=RIDGE,
                                bg="#0676ad", fg="white")
        self.lbl_student.place(x=455, y=400, width=200, height=70)
        self.lbl_Result = Label(self.root, text="Total Result\n[0]", font=("goudy old style", 15), bd=10, relief=RIDGE,
                                 bg="#038074", fg="white")
        self.lbl_Result.place(x=660, y=400, width=200, height=70)
# footer
        footer = Label(self.root, text="SRM-Student Result Management System\n Contact us at:021-xxxxxx", font=("goudy old style", 15, 'bold'),
                      bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    def report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)


if __name__=="__main__":
   root=Tk()
   obj=RMS(root)
   root.mainloop()
