import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x450+0+60")
        self.root.title("Result Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        title = Label(self.root, text="Add Student Result Details", font=("goudy old style", 20, 'bold'), bg="orange",fg="#262626").pack(fill=X,ipadx=50)
        #variables
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_course = StringVar()
        self.var_marksobt = StringVar()
        self.var_markstotal = StringVar()
        self.roll_List=[]

        #labels=
        lbl_rollno = Label(self.root, text="Select Students", font=("goudy old style", 20, 'bold'), bg="white").place(x=10,y=70)
        lbl_name= Label(self.root, text="Name", font=("goudy old style", 20, 'bold'), bg="white").place(x=10,y=140)
        lbl_rollno = Label(self.root, text="Course", font=("goudy old style", 20, 'bold'), bg="white").place(
            x=10, y=210)
        lbl_marksobt = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, 'bold'), bg="white").place(
            x=10, y=280)
        lbl_totalmarks= Label(self.root, text="Total Marks", font=("goudy old style", 20, 'bold'), bg="white").place(
            x=10, y=350)
        #entries
        self.rollno_List=[]
        self.fetch_rollno()
        self.txt_students = ttk.Combobox(self.root, textvariable=self.var_rollno, font=("goudy old style", 20, 'bold'),
                                       values=self.rollno_List, state="readonly", justify="center")
        self.txt_students.place(x=200, y=70, width=250)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'),state="readonly",
                              bg="lightyellow")
        self.txt_name.place(x=200, y=140, width=375)
        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, 'bold'),state="readonly",
                              bg="lightyellow")
        self.txt_course.place(x=200, y=210, width=375)
        self.txt_marksobtain = Entry(self.root, textvariable=self.var_marksobt, font=("goudy old style", 20, 'bold'),
                              bg="lightyellow")
        self.txt_marksobtain.place(x=200, y=280, width=375)
        self.txt_totalmarks = Entry(self.root, textvariable=self.var_markstotal, font=("goudy old style", 20, 'bold'),
                              bg="lightyellow")
        self.txt_totalmarks.place(x=200, y=340, width=375)
        #Button
        self.search_button = Button(self.root, text="Search", font=("goudy old style", 15, 'bold'), bg="#03a9f4",
                                    fg="white",
                                    cursor='hand2',command=self.search)
        self.search_button.place(x=470, y=68, width=110, height=42)
        self.add_button = Button(self.root, text="Save", font=("goudy old style", 15, 'bold'), bg="#219653",activebackground="lightgreen", fg="white",
                                 cursor='hand2',command=self.add)
        self.add_button.place(x=300, y=390, width=110, height=40)
        self.Clear_button = Button(self.root, text="Clear", font=("goudy old style", 15, 'bold'), bg="#607d86",activebackground="lightgrey",
                                   fg="white", cursor='hand2',command=self.clear)
        self.Clear_button.place(x=420, y=390, width=110, height=40)
        #image
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((460, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=600, y=70, width=460, height=300)

    def fetch_rollno(self):
            rms = mysql.connector.connect(
                host='localhost',
                user='root',
                password='fundraisors123',
                port=3306,
                database='rms'

            )
            mycursor = rms.cursor()
            mycursor.execute("select rollno from student")
            rows = mycursor.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.rollno_List.append(row[0])

            rms.commit()
    def search(self):
       rms=mysql.connector.connect(
           host='localhost',
           username='root',
           password='fundraisors123',
           port=3306,
           database='rms'

       )
       mycursor=rms.cursor()
       mycursor.execute("select name,course from student where rollno=%s",(self.var_rollno.get(),))
       row=mycursor.fetchone()
       if row!=None:
          self.var_name.set(row[0])
          self.var_course.set(row[1])

       else:
           messagebox.showerror("Error","No record found",parent=self.root)

    def add(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()

        if self.var_name.get() == "":
            messagebox.showerror("Error", "First search student record", parent=self.root)

        else:

            mycursor.execute("select * from result where rollno=%s and course=%s", (self.var_rollno.get(),self.var_course.get()))

            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Result  already present", parent=self.root)
            else:
                per=((int(self.var_marksobt.get()))/int(self.var_markstotal.get()))*100
                mycursor.execute("insert into result values(%s,%s,%s,%s,%s,%s)", (
                    int(self.var_rollno.get()),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marksobt.get(),
                    self.var_markstotal.get(),
                    str(per)
                ))
                rms.commit()
                messagebox.showinfo("Success", "Result Added successfully", parent=self.root)

    def clear(self):
        (self.var_rollno.set("")),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marksobt.set(""),
        self.var_markstotal.set(""),



if __name__=="__main__":
   root=Tk()
   obj=ResultClass(root)
   root.mainloop()