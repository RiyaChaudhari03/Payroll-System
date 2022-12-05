from tkinter import *
from tkinter import ttk
import pymysql
import pymysql.cursors
win = Tk()
win.geometry("800x450")
style = ttk.Style()
style.theme_use('clam')
tree = ttk.Treeview(win, column=("Employee Number", "Name", "Month","No. of Days","No. of Leaves","Overtime(in hrs.)","Salary","Salary/day","Deduction","Extratime","Grosspay"), show='headings', height=30)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Employee Number")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Month")
tree.column("# 4", anchor=CENTER)
tree.heading("#4", text="No. of Days")
tree.column("# 5", anchor=CENTER)
tree.heading("#5", text="NO.of Leaves")
tree.column("# 6", anchor=CENTER)
tree.heading("#6", text="Overtime(in hrs.)")
tree.column("# 7", anchor=CENTER)
tree.heading("#7", text="Salary")
tree.column("# 8", anchor=CENTER)
tree.heading("#8", text="Salary/day")
tree.column("# 9", anchor=CENTER)
tree.heading("#9", text="Deduction")
tree.column("# 10", anchor=CENTER)
tree.heading("#10", text="Extratime")
tree.column("# 11", anchor=CENTER)
tree.heading("#11", text="Grosspay")
conn=pymysql.connect(host='localhost',user='root',db='payroll')
a=conn.cursor()
sql="SELECT * FROM salary"
try:
    numrows=a.execute(sql)
    results=a.fetchall()
    for row in results:
        empno=row[0]
        name=row[1]
        month=row[2]
        ndays=row[3]
        nleaves=row[4]
        otime=row[5]
        salary=row[6]
        spday=row[7]
        deduct=row[8]
        etime=row[9]
        gpay=row[10]
        tree.insert('','end', text="1", values=(empno,name,month,ndays,nleaves,otime,salary,spday,deduct,etime,gpay))
except:
            print("ERROR")
a.close()
conn.close()
tree.pack()
win.mainloop()
