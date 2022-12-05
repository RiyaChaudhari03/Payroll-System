from tkinter import *
from tkinter import ttk
import pymysql
import pymysql.cursors
win = Tk()
win.geometry("700x350")
style = ttk.Style()
style.theme_use('clam')
tree = ttk.Treeview(win, column=("Employee Number", "Name", "Qualification","Experience","Job","Date Of Join","Contact","Address","Email","Salary"), show='headings', height=15)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Employee Number")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Qualificatio")
tree.column("# 4", anchor=CENTER)
tree.heading("#4", text="Experience")
tree.column("# 5", anchor=CENTER)
tree.heading("#5", text="Job")
tree.column("# 6", anchor=CENTER)
tree.heading("#6", text="Date Of Join")
tree.column("# 7", anchor=CENTER)
tree.heading("#7", text="Contact")
tree.column("# 8", anchor=CENTER)
tree.heading("#8", text="Address")
tree.column("# 9", anchor=CENTER)
tree.heading("#9", text="Email")
tree.column("# 10", anchor=CENTER)
tree.heading("#10", text="Salary")
conn=pymysql.connect(host='localhost',user='root',db='payroll')
a=conn.cursor()
sql="SELECT * FROM employee"
try:
    numrows=a.execute(sql)
    results=a.fetchall()
    for row in results:
        empno=row[0]
        name=row[1]
        qlfn=row[2]
        exp=row[3]
        job=row[4]
        doj=row[5]
        contact=row[6]
        address=row[7]
        email=row[8]
        salary=row[9]
        tree.insert('','end', text="1", values=(empno,name,qlfn,exp,job,doj,contact,address,email,salary))
except:
            print("ERROR")
a.close()
conn.close()
tree.pack()
win.mainloop()
