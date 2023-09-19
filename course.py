from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
class CourseClass:
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
        title = Label(self.root, text="Manage Course", font=("goudy old style", 20, 'bold'),bg="#033054",  fg='white').pack(fill=X)
        #VARIABLES
        self.var_cid=StringVar()
        self.var_course=StringVar()
        self.var_duration = StringVar()
        self.var_charges= StringVar()

        #labels
        lbl_Course_Id=Label(self.root,text="Course ID",font=("goudy old style", 15, 'bold'),bg="white").place(x=10,y=50)
        lbl_Course_name=Label(self.root,text="Course Name",font=("goudy old style", 15, 'bold'),bg="white").place(x=10,y=90)
        lbl_Duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_Charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg="white").place( x=10, y=170)
        lbl_Descriptio = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=210)
        #entry
        self.txt_Course_Id = Entry(self.root, textvariable=self.var_cid, font=("goudy old style", 15, 'bold'),bg="lightyellow")
        self.txt_Course_Id.place(x=150, y=50, width=200)
        self.txt_Course_name = Entry(self.root,textvariable=self.var_course,  font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Course_name.place(x=150, y=90,width=200)
        self.txt_Duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Duration.place(x=150 ,y=130,width=200)
        self.txt_Charges = Entry(self.root,  textvariable=self.var_charges,font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Charges.place(x=150,y=170,width=200)
        self.txt_Description =Text(self.root,  font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_Description.place(x=150, y=210,width=500,height=130)
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
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style", 15, 'bold'),bg="white").place(x=720,y=60)
        self.search_Course_name = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'),
                                     bg="lightyellow").place(x=850, y=60, width=200)
        self.search_button = Button(self.root, text="Search", font=("goudy old style", 15, 'bold'), bg="#03a9f4", fg="white",
                                 cursor='hand2',command=self.search)
        self.search_button.place(x=900, y=90, width=110, height=40)
        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=700,y=150,width=375,height=300)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        self.CTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CTable.xview)
        scrolly.config(command=self.CTable.yview)
        self.CTable.heading("cid",text="Course ID")
        self.CTable.heading("name", text="Course Name")
        self.CTable.heading("duration", text="Duration")
        self.CTable.heading("charges", text="Charges")
        self.CTable.heading("description", text="Description")
        self.CTable['show']='headings'
        self.CTable.column("cid", width=80)
        self.CTable.column("name", width=80)
        self.CTable.column("duration", width=80)
        self.CTable.column("charges", width=80)
        self.CTable.column("description", width=100)
        self.CTable.pack(fill=BOTH,expand=1)
        self.CTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    def get_data(self,ev):
        self.txt_Course_Id.config(state="readonly")
        self.txt_Course_Id
        r=self.CTable.focus()
        content=self.CTable.item(r)
        row=content["values"]
        #print(row)
        self.var_cid.set(row[0])
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
       # self.txt_Description.set(row[4])
        self.txt_Description.delete('1.0',END)
        self.txt_Description.insert(END,row[4])
    def add(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor=rms.cursor()


        if self.var_course.get()=="":
             messagebox.showerror("Error","Course Id Name is required",parent=self.root)
        elif (self.var_cid.get())=="":
            messagebox.showerror("Error", "Course Id  is required", parent=self.root)

        else:

             mycursor.execute("select * from course where name=%s",(self.var_course.get(),))



             row=mycursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","Course Name already present",parent=self.root)
             else:
                 mycursor.execute("insert into course values(%s,%s,%s,%s,%s)",(
                     int(self.var_cid.get()),
                     self.var_course.get(),
                     self.var_duration.get(),
                     self.var_charges.get(),
                     self.txt_Description.get("1.0",END)
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


        if self.var_course.get()=="":
             messagebox.showerror("Error","Course  Name is required",parent=self.root)
        elif (self.var_cid.get())=="":
            messagebox.showerror("Error", "Course Id  is required", parent=self.root)

        else:

             mycursor.execute("select * from course where cid=%s",(self.var_cid.get(),))


             row=mycursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Select Course from list",parent=self.root)
             else:
                 mycursor.execute("update course set name=%s,duration=%s,charges=%s,description=%s where cid=%s",(

                     self.var_course.get(),
                     self.var_duration.get(),
                     self.var_charges.get(),
                     self.txt_Description.get("1.0",END),
                     int(self.var_cid.get()),



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
        mycursor.execute("select * from course")
        rows=mycursor.fetchall()
        self.CTable.delete(*self.CTable.get_children())
        for row in rows:
            self.CTable.insert('',END,values=row)
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
       mycursor.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
       rows=mycursor.fetchall()
       if len(rows)!=0:
           self.CTable.delete(* self.CTable.get_children())
           for row in rows:
              self.CTable.insert('',END,values=row)
       else:
           messagebox.showerror("Error","No such Course exist")



    def clear(self):
        self.show()
        self.var_cid.set("")
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_Description.delete('1.0',END)
        self.txt_Course_Id.config(state=NORMAL)
    def delete(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()

        if self.var_course.get() == "":
            messagebox.showerror("Error", "Course Id Name is required", parent=self.root)
        elif (self.var_cid.get()) == "":
            messagebox.showerror("Error", "Course Id  is required", parent=self.root)

        else:

            mycursor.execute("select * from course where name=%s", (self.var_course.get(),))

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select Course from the List first", parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                if op==True:
                    mycursor.execute("delete from course where name=%s",(self.var_course.get(),))
                    rms.commit()
                    messagebox.showinfo("Delete", "Course Deleted successfully", parent=self.root)
                    self.clear()



















if __name__=="__main__":
   root=Tk()
   obj=CourseClass(root)
   root.mainloop()