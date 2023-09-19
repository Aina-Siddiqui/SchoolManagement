import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

class Student():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Database")
        self.root.geometry("1000x1000")
        self.root.config(bg="white")
        head=Label(self.root,text="STUDENT DATABASE MANAGEMENT SYSTEM",font=("Verdana",30),bg="#30549c")
        head.pack(fill=X,ipady=5)
        photo=Image.open("studentdatabse.jpg")


        img=ImageTk.PhotoImage(photo)

        img_label = Label(self.root,image=img)
        img_label.image=img

        img_label.place(x= 10,y=70)
        nam1=Label(self.root,text="Name",font=('Bahnschrift',20))
        nam1.place(x=275,y=75)





        mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            password='fundraisors123',
            port='3306',
            database='sd'
    )

class Student():
   root=Tk()
   obj=Student(root)
   root.mainloop()
