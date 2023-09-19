from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class StudentClass:
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
        # title
        title = Label(self.root, text="Manage Student Detail", font=("goudy old style", 20, 'bold'),bg="#033054",  fg='white').pack(fill=X)
        #VARIABLES
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email = StringVar()
        self.var_gender= StringVar()
        self.var_dob = StringVar()
        self.var_contactno = StringVar()
        self.var_course=StringVar()

        #labels
        lbl_rollno=Label(self.root,text="Roll no",font=("goudy old style", 15, 'bold'),bg="white").place(x=10,y=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style", 15, 'bold'),bg="white").place(x=10,y=90)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg="white").place( x=10, y=170)
        lbl_dob = Label(self.root, text="DOB", font=("goudy old style", 15, 'bold'), bg="white").place(x=10,y=210)

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg="white").place(x=10,y=250)
        lbl_contact = Label(self.root, text="Contact No", font=("goudy old style", 15, 'bold'), bg="white").place(x=370, y=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg="white").place(x=370,y=90)

        #entry
        self.course_List=["Empty"]
        self.fetch_course()
        self.txt_roll= Entry(self.root, textvariable=self.var_rollno, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_roll.place(x=150, y=50, width=200)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_name.place(x=150, y=90, width=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_email.place(x=150, y=130, width=200)
        self.txt_Gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=['Select','Male','Female','Other'], font=("goudy old style", 15, 'bold'),state="readonly",justify="center")
        self.txt_Gender.place(x=150,y=170,width=200)
        self.txt_Gender.current(0)
        self.txt_DOB = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, 'bold'),
                               bg="lightyellow")
        self.txt_DOB.place(x=150, y=210, width=200)
        self.txt_address =Text(self.root, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_address.place(x=150, y=250, width=450, height=100)
        self.txt_contact = Entry(self.root, textvariable=self.var_contactno, font=("goudy old style", 15, 'bold'),
                               bg="lightyellow")
        self.txt_contact.place(x=480, y=50, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,font=("goudy old style", 15, 'bold'),values=self.course_List ,state="readonly", justify="center")
        self.txt_course.place(x=480, y=90, width=200)
        #Buttons
        self.add_button=Button(self.root,text="Save",font=("goudy old style", 15, 'bold'),bg="#219653",fg="white",cursor='hand2',command=self.add)
        self.add_button.place(x=150,y=400,width=110,height=40)
        self.update_button = Button(self.root, text="Update", font=("goudy old style", 15, 'bold'), bg="#4caf50", fg="white",
                                 cursor='hand2',command=self.update)
        self.update_button.place(x=270, y=400, width=110, height=40)
        self.Del_button = Button(self.root, text="Delete", font=("goudy old style", 15, 'bold'), bg="#f44336",fg="white",cursor='hand2',command=self.delete)
        self.Del_button.place(x=390, y=400, width=110, height=40)
        self.Clear_button = Button(self.root, text="Clear", font=("goudy old style", 15, 'bold'), bg="#607d86",fg="white", cursor='hand2',command=self.clear)
        self.Clear_button.place(x=510, y=400, width=110, height=40)
        #searcg panel
        self.var_search=StringVar()
        lbl_search_rollno=Label(self.root,text="Roll No",font=("goudy old style", 15, 'bold'),bg="white").place(x=720,y=60)
        self.search_rollno = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'),
                                     bg="lightyellow").place(x=800, y=60, width=195)
        self.search_button = Button(self.root, text="Search", font=("goudy old style", 15, 'bold'), bg="#03a9f4", fg="white",
                                 cursor='hand2',command=self.search)
        self.search_button.place(x=1000, y=60, width=105, height=30)
        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=700,y=112,width=375,height=330)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.CTable=ttk.Treeview(self.C_Frame,columns=("rollno","name","email","gender","dob","address","contactno","course"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CTable.xview)
        scrolly.config(command=self.CTable.yview)
        self.CTable.heading("rollno",text="Roll No")
        self.CTable.heading("name", text="Name")
        self.CTable.heading("email", text="Email ID")
        self.CTable.heading("gender", text="Gender")
        self.CTable.heading("dob", text="DOB")
        self.CTable.heading("address", text="Address")
        self.CTable.heading("contactno", text="Contact No")
        self.CTable.heading("course", text="Course")

        self.CTable['show']='headings'
        self.CTable.column("rollno", width=80)
        self.CTable.column("name", width=80)
        self.CTable.column("email", width=100)
        self.CTable.column("gender", width=80)
        self.CTable.column("dob", width=80)
        self.CTable.column("address", width=100)
        self.CTable.column("contactno", width=100)
        self.CTable.column("course", width=80)

        self.CTable.pack(fill=BOTH,expand=1)
        self.CTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_course()
    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
      # self.txt_roll
        r=self.CTable.focus()
        content=self.CTable.item(r)
        row=content["values"]
        #print(row)
        self.var_rollno.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END,row[5]),
        self.var_contactno.set(row[6]),
        self.var_course.set(row[7]),

       # self.txt_Description.set(row[4])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[4])
    def add(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor=rms.cursor()


        if self.var_name.get()== "":
             messagebox.showerror("Error","Name is required",parent=self.root)
        elif (self.var_rollno.get())== "":
            messagebox.showerror("Error", "Roll no  is required", parent=self.root)

        else:

             mycursor.execute("select * from student where rollno=%s", (self.var_rollno.get(),))



             row=mycursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","Roll Number already present",parent=self.root)
             else:
                 mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                     int(self.var_rollno.get()),
                     self.var_name.get(),
                     self.var_email.get(),
                     self.var_gender.get(),
                     self.var_dob.get(),
                     self.txt_address.get("1.0", END),
                     self.var_contactno.get(),
                     self.var_course.get(),
                 ))
                 rms.commit()
                 messagebox.showinfo("Success","Course Added successfully",parent=self.root)
                 self.show()
    def update(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor=rms.cursor()


        if self.var_name.get()== "":
             messagebox.showerror("Error","Name is required",parent=self.root)
        elif (self.var_rollno.get())== "":
            messagebox.showerror("Error", "Roll no   is required", parent=self.root)

        else:

             mycursor.execute("select * from student where rollno=%s", (self.var_rollno.get(),))


             row=mycursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Roll no not present",parent=self.root)
             else:
                 mycursor.execute("update student set name=%s,email=%s,gender=%s,dob=%s,address=%s,contactno=%s,course=%s where rollno=%s",(


                     self.var_name.get(),
                     self.var_email.get(),
                     self.var_gender.get(),
                     self.var_dob.get(),
                     self.txt_address.get("1.0", END),
                     self.var_contactno.get(),
                     self.var_course.get(),
                     int(self.var_rollno.get()),



                 ))
                 rms.commit()
                 messagebox.showinfo("Success","Course updated successfully",parent=self.root)
                 self.show()


    def show(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()
        mycursor.execute("select * from student")
        rows=mycursor.fetchall()
        self.CTable.delete(*self.CTable.get_children())
        for row in rows:
            self.CTable.insert('',END,values=row)
        rms.commit()
        rms.close()
    def fetch_course(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()
        mycursor.execute("select name from course")
        rows=mycursor.fetchall()

        if len(rows)>0:
            for row in rows:
               self.course_List.append(row[0])


        rms.commit()
        rms.close()

    def search(self):
       rms=mysql.connector.connect(
           host='localhost',
           username='root',
           password='fundraisors123',
           port=3306,
           database='rms'

       )
       mycursor=rms.cursor()
       mycursor.execute("select * from student where rollno=%s",(self.var_search.get(),))
       row=mycursor.fetchone()
       if row!=None:
           self.CTable.delete(* self.CTable.get_children())

           self.CTable.insert('',END,values=row)
       else:
           messagebox.showerror("Error","No record found",parent=self.root)



    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_search.set("")
        self.txt_address.delete('1.0', END)
        self.txt_roll.config(state=NORMAL)
        self.var_dob.set("")
        self.var_course.set("")
        self.var_contactno.set("")
    def delete(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()

        if self.var_name.get() == "":
            messagebox.showerror("Error", " Name is required", parent=self.root)
        elif (self.var_rollno.get()) == "":
            messagebox.showerror("Error", "Rollno is required", parent=self.root)

        else:

            mycursor.execute("select * from student where rollno=%s", (self.var_rollno.get(),))

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select Course from the List first", parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                if op==True:
                    mycursor.execute("delete from student where rollno=%s", (self.var_rollno.get(),))
                    rms.commit()
                    messagebox.showinfo("Delete", "Course Deleted successfully", parent=self.root)
                    self.clear()



















if __name__=="__main__":
   root=Tk()
   obj=StudentClass(root)
   root.mainloop()