import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='fundraisors123',
    port=3306,
    database="rms"

)
cur=mydb.cursor()
cur.execute("select * from course")
row=cur.fetchall()
for i in row:
    print(i)
