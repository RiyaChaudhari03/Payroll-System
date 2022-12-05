from tkinter import *
from PIL import ImageTk, Image
import pymysql
import pymysql.cursors


def onselect(evt):
    # q1
    global job
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    standard = value
    e101.delete(0, END)
    e101.insert(END, standard)
    print('you selected item %d:""%s"' % (index, value))

def add_fields():
    conn = pymysql.connect(host='localhost', user='root', db='payroll')
    a = conn.cursor()
    a1 = e1.get()
    a2 = e2.get()
    a3 = e3.get()
    a4 = e4.get()
    a5 = e101.get()
    a6 = e6.get()
    a7 = e7.get()
    a8 = e8.get()
    a9 = e9.get()
    a10 = e10.get()
    insertstmt = (
            "insert into employee(employeeno,name,qualification,experience,job,dateofjoin,contact,address,email,"
            "salary) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
    a.execute(insertstmt)
    L1.config(text="Employee Added", fg="#00008b", font=("times", 20))
    conn.commit()
    a.close()
    conn.close()
    print(
        "EMPLOYEENO:%s\nNAME:%s\nQUALIFICATION:%s\nEXPERIENCE:%s\nJOB:%s\nDATEOFJOIN:%s\nCONTACT:%s\nADDRESS:%s"
        "\nEMAIL:%s\nSALARY:%s" % (
            e1.get(), e2.get(), e3.get(), e4.get(), e101.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get()))


def PRODUCT():

    k1.insert(END, "Programmer")
    k1.insert(END, "Tester")
    k1.insert(END, "Database administrator")
    k1.insert(END, "Web Developer")



master = Tk()
master.title("inventary")
img = Image.open('a1.jpg')
bg = ImageTk.PhotoImage(img)
master.geometry("750x450")
label3 = Label(master, image=bg)
label3.place(x=0, y=0)

label = Label(master, text="ADD EMPLOYEE", fg="#00008b", font=("times", 20))
label.place(x=300, y=25)
label1 = Label(master, text="EMPLOYEE NO.", fg="#00008b", font=("times", 15))
label1.place(x=30, y=80)
label2 = Label(master, text="NAME", fg="#00008b", font=("times", 15))
label2.place(x=30, y=110)
label3 = Label(master, text="QUALIFICATION", fg="#00008b", font=("times", 15))
label3.place(x=30, y=140)
label4 = Label(master, text="EXPERIENCE", fg="#00008b", font=("times", 15))
label4.place(x=30, y=170)
label5 = Label(master, text="JOB", fg="#00008b", font=("times", 15))
label5.place(x=30, y=200)

label6 = Label(master, text="DATE OF JOINING", fg="#00008b", font=("times", 15))
label6.place(x=30, y=230)  # Format year-mon-day
label7 = Label(master, text="CONTACT", fg="#00008b", font=("times", 15))
label7.place(x=30, y=260)
label8 = Label(master, text="ADDRESS", fg="#00008b", font=("times", 15))
label8.place(x=30, y=290)
label9 = Label(master, text="EMAIL", fg="#00008b", font=("times", 15))
label9.place(x=30, y=320)

label10 = Label(master, text="SALARY", fg="#00008b", font=("times", 15))
label10.place(x=30, y=350)
e1 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e2 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e3 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e4 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
k1 = Listbox(master, height=3)
k1.place(x=200, y=200)
k1.bind("<Double-1>", onselect)
e6 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e7 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e8 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e9 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e10 = Entry(master, width=40, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")

e1.place(x=200, y=80)
e2.place(x=200, y=110)
e3.place(x=200, y=140)
e4.place(x=200, y=170)
e101 = Entry(master, width=23, bd=4, fg="white", bg="#00008b", font="italic", selectbackground="cyan")
e101.place(x=350, y=200)
e6.place(x=200, y=230)
e7.place(x=200, y=260)
e8.place(x=200, y=290)
e9.place(x=200, y=320)
e10.place(x=200, y=350)

Button(master, text="ADD", fg="#00008b", command=add_fields).place(x=30, y=380)
Button(master, text="Close", fg="#00008b", command=master.quit).place(x=200, y=380)

L1 = Label(master, text="")
L1.place(x=400, y=420)
PRODUCT()
mainloop()
