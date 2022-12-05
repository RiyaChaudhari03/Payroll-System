import os
from tkinter import *

import pymysql
import pymysql.cursors


def search_id():
    conn = pymysql.connect(host='localhost', user='root', db='payroll')
    a = conn.cursor()
    uid = e1.get()
    pwd = e2.get()
    sql = "SELECT * FROM admin where uid='%s' and  pass='%s'" % (uid, pwd)
    try:
        a.execute(sql)
        p = a.rowcount
        if p >= 1:
            os.system('python MainWindow.py')
            print("ok")
        else:
            print("invalid uid")
    except:
        print("ERROR")
    a.close()
    conn.close()


master = Tk()
master.title("Payroll Management System")
master.configure(bg="#375068")
Label(master, text="Admin Login", fg="white", bg="#375068", font=("times", 20)).grid(column=1)
Label(master, text=" USER ID", fg="white", bg="#375068", font=("times", 13)).grid(row=1)
Label(master, text=" PAASWORD", fg="white", bg="#375068", font=("times", 13)).grid(row=2)
e1 = Entry(master, width=30, bd=4, fg="blue", bg="#F7EE89")
e2 = Entry(master, width=30, show="*", bd=4, fg="blue", bg="#F7EE89")
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
Button(master, text="Login", fg="blue", command=search_id).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text="Cancel", fg="blue", command=master.quit).grid(row=3, column=2, sticky=W, pady=4)
mainloop()
