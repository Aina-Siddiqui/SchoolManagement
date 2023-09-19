import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
class ReportClass:
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

        title = Label(self.root, text="View Student Result", font=("goudy old style", 20, 'bold'), bg="orange",
                      fg="#262626").pack(fill=X, ipady=10)
        #variable
        self.var_search=StringVar()
        #search
        lbl_search = Label(self.root, text="Search By Roll No", font=("goudy old style", 20, 'bold'), bg="white").place(
            x=10, y=70)
        txt_search = Entry(self.root,textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow").place(
            x=250, y=70)
        #button
        self.search_button = Button(self.root, text="Search", font=("goudy old style", 15, 'bold'), bg="#03a9f4",
                                    fg="white",
                                    cursor='hand2',command=self.search)
        self.search_button.place(x=550, y=68, width=130, height=38)
        self.clear_button = Button(self.root, text="Clear", font=("goudy old style", 15, 'bold'), bg="grey",
                                    fg="white",
                                    cursor='hand2',command=self.clear)
        self.clear_button.place(x=700, y=68, width=130, height=38)
        #labels
        lbl_roll=Label(self.root,text="Roll no ",font=("goudy old style", 20, 'bold'),bg="white",bd=2,relief=GROOVE).place(x=100,y=130,width=150,height=50)
        lbl_name = Label(self.root, text="Name ", font=("goudy old style", 20, 'bold'), bg="white", bd=2,
                         relief=GROOVE).place(x=250, y=130, width=150, height=50)
        lbl_course = Label(self.root, text="Course ", font=("goudy old style", 20, 'bold'), bg="white", bd=2,
                         relief=GROOVE).place(x=400, y=130, width=150, height=50)
        lbl_marksobt = Label(self.root, text="Marks Obtained ", font=("goudy old style", 16, 'bold'), bg="white", bd=2,
                           relief=GROOVE).place(x=550, y=130, width=150, height=50)
        lbl_total = Label(self.root, text="Total Marks ", font=("goudy old style", 16, 'bold'), bg="white", bd=2,
                           relief=GROOVE).place(x=700, y=130, width=150, height=50)
        lbl_percentage = Label(self.root, text="Percentage ", font=("goudy old style", 16, 'bold'), bg="white", bd=2,
                           relief=GROOVE).place(x=850, y=130, width=150, height=50)
        self.roll = Label(self.root,  font=("goudy old style", 20, 'bold'), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=100, y=180, width=150, height=50)
        self.name = Label(self.root,  font=("goudy old style", 20, 'bold'), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=250, y=180, width=150, height=50)
        self.course = Label(self.root, font=("goudy old style", 20, 'bold'), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=400, y=180, width=150, height=50)
        self.marksobt = Label(self.root,  font=("goudy old style", 16, 'bold'), bg="white", bd=2, relief=GROOVE)
        self.marksobt.place(x=550, y=180, width=150, height=50)
        self.total = Label(self.root, font=("goudy old style", 16, 'bold'), bg="white", bd=2,relief=GROOVE)
        self.total.place(x=700, y=180, width=150, height=50)
        self.per = Label(self.root,  font=("goudy old style", 16, 'bold'), bg="white", bd=2,relief=GROOVE)
        self.per.place(x=850, y=180, width=150, height=50)
        #button
        self.delete_button = Button(self.root, text="Delete", font=("goudy old style", 15, 'bold'), bg="red",
                                   fg="white",
                                   cursor='hand2',command=self.delete)
        self.delete_button.place(x=450, y=250, width=130, height=45)

    def search(self):
        rms = mysql.connector.connect(
            host='localhost',
            username='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()
        if self.var_search.get()=="":
            messagebox.showerror("Error","Roll no  is required",parent=self.root)
        else:
            mycursor.execute("select * from result where rollno=%s", (self.var_search.get(),))
            row = mycursor.fetchone()

            if row != None:
                self.roll.config(text=row[0])
                self.name.config(text=row[1])
                self.course.config(text=row[2])
                self.marksobt.config(text=row[3])
                self.total.config(text=row[4])
                self.per.config(text=row[5])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
    def clear(self):
       self.roll.config(text="")
       self.name.config(text="")
       self.course.config(text="")
       self.marksobt.config(text="")
       self.total.config(text="")
       self.per.config(text="")
       self.var_search.set("")
    def delete(self):
        rms = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port=3306,
            database='rms'

        )
        mycursor = rms.cursor()


        if (self.var_search.get()) == "":
            messagebox.showerror("Error", "Rollno is required", parent=self.root)

        else:

            mycursor.execute("select * from result where rollno=%s", (self.var_search.get(),))

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select Course from the List first", parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                if op==True:
                    mycursor.execute("delete from result where rollno=%s", (self.var_search.get(),))
                    rms.commit()
                    messagebox.showinfo("Delete", "Course Deleted successfully", parent=self.root)
                    self.clear()


if __name__=="__main__":
   root=Tk()
   obj=ReportClass(root)
   root.mainloop()
