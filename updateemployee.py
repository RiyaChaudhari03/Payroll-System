from tkinter import*
from PIL import ImageTk, Image  
import pymysql
import pymysql.cursors

def onselect(evt):
    global job
    w=evt.widget
    index=int(w.curselection()[0])
    value=w.get(index)
    job=value
    e101.delete(0,END)
    e101.insert(END,job)
    print('you selected item %d:""%s"'%(index,value))
def search_record():
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    args=int(e11.get())
    sql="SELECT * FROM employee where employeeno=%d"%(args)
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
            e1.insert(0,empno)
            e2.insert(1,name)
            e3.insert(2,qlfn)
            e4.insert(3,exp)
            e101.insert(4,job)
            e6.insert(5,doj)
            e7.insert(6,contact)
            e8.insert(7,address)
            e9.insert(8,email)
            e10.insert(9,salary)
    except:
        print("ERROR")
        a.close()
        conn.close()

def update_record():
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    args1=e2.get()
    args2=e3.get()
    args3=e4.get()
    args4=e101.get()
    args5=e6.get()
    args6=e7.get()
    args7=e8.get()
    args8=e9.get()
    args9=e10.get()
    args10=int(e11.get())
    
    L1.config(text="Emloyee Updated",fg="#3a3b3c",font=("times",20))
    sqlupd="UPDATE employee SET name='%s',qualification='%s',experience='%s',job='%s',dateofjoin='%s',contact='%s',address='%s',email='%s',salary='%s' WHERE employeeno=%d"%(args1,args2,args3,args4,args5,args6,args7,args8,args9,args10)
    a.execute(sqlupd)
    print("Record updated")
    conn.commit()
    a.close()
    conn.close()
def PRODUCT():
    k1.insert(END,"Programmer")
    k1.insert(END,"Tester")
    k1.insert(END,"Database administrator")
    k1.insert(END,"Web Developer")
master=Tk()
master.title("inventary")
img =Image.open('a1.jpg')
bg = ImageTk.PhotoImage(img)
master.geometry("750x450")
label3 = Label(master, image=bg)
label3.place(x =0,y =0)

label=Label(master,text="UPDATE EMPLOYEE",fg="#3a3b3c",font=("times",20))
label.place(x=300,y=25)
label1=Label(master,text="EMPLOYEE NO.",fg="#3a3b3c",font=("times",15))
label1.place(x=30,y=80)
label2=Label(master,text="NAME",fg="#3a3b3c",font=("times",15))
label2.place(x=30,y=110)
label3=Label(master,text="QUALIFICATION",fg="#3a3b3c",font=("times",15))
label3.place(x=30,y=140)
label4=Label(master,text="EXPERIENCE",fg="#3a3b3c",font=("times",15))
label4.place(x=30,y=170)
label5=Label(master,text="JOB",fg="#3a3b3c",font=("times",15))
label5.place(x=30,y=200)

label6=Label(master,text="DATE OF JOINING",fg="#3a3b3c",font=("times",15))
label6.place(x=30,y=230)
label7=Label(master,text="CONTACT",fg="#3a3b3c",font=("times",15))
label7.place(x=30,y=260)
label8=Label(master,text="ADDRESS",fg="#3a3b3c",font=("times",15))
label8.place(x=30,y=290)
label9=Label(master,text="EMAIL",fg="#3a3b3c",font=("times",15))
label9.place(x=30,y=320)

label10=Label(master,text="SALARY",fg="#3a3b3c",font=("times",15))
label10.place(x=30,y=350)
label11=Label(master,text="SEARCH EMPLOYEE NO",fg="#3a3b3c",font=("times",15))
label11.place(x=30,y=380)

e1=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e2=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e3=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e4=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
k1=Listbox(master,height=2)
k1.place(x=250,y=200)
k1.bind("<Double-1>",onselect)
e6=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e7=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e8=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e9=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e10=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e11=Entry(master,width=40,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e1.place(x=250,y=80)
e2.place(x=250,y=110)
e3.place(x=250,y=140)
e4.place(x=250,y=170)
e101=Entry(master,width=23,bd=4,fg="white",bg="#3a3b3c",font="italic",selectbackground="cyan")
e101.place(x=400,y=200)
e6.place(x=250,y=230)
e7.place(x=250,y=260)
e8.place(x=250,y=290)
e9.place(x=250,y=320)
e10.place(x=250,y=350)
e11.place(x=250,y=380)
Button(master,text="SEARCH",fg="#3a3b3c",command=search_record).place(x=30,y=410)
Button(master,text="UPDATE",fg="#3a3b3c",command=update_record).place(x=200,y=410)
Button(master,text="CLOSE",fg="#3a3b3c",command=master.quit).place(x=370,y=410)

L1=Label(master,text="")
L1.place (x=400,y=450)
PRODUCT()
mainloop()
