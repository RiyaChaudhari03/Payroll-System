from tkinter import*
from PIL import ImageTk, Image  
import pymysql
import pymysql.cursors
deduction=0
spday=0
extratime=0
grosspay=0



def search_record():
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    args=int(e12.get())
    sql="SELECT * FROM employee where employeeno=%d"%(args)
    try:
       numrows=a.execute(sql)
       results=a.fetchall()
       for row in results:
            empno=row[0]
            name=row[1]
            sal=row[9]
            e1.insert(0,empno)
            e2.insert(0,name)
            e7.insert(0,sal)
           
    except:
        print("ERROR")
        a.close()
        conn.close()

   
def add_fields():
    ndays=int(e4.get())
    nleaves=int(e5.get())
    overtime=int(e6.get())
    salary=int(e7.get())
  
   
    spday=salary/30
    phour=spday/8
    extratime=overtime*phour*2
    deduction=spday*nleaves
    
    grosspay=(salary-deduction)+extratime
    print(salary)
    print(deduction)
    print(extratime)
    print(grosspay)
    
    e8.insert(0,spday)
    e9.insert(0,deduction)
    e10.insert(0,extratime)
    e11.insert(0,grosspay)
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    a1=e1.get()
    a2=e2.get()
    a3=e101.get()
    a4=e4.get()
    a5=e5.get()
    a6=e6.get()
    a7=e7.get()
    a8=e8.get()
    a9=e9.get()
    a10=e10.get()
    a11=e11.get()
    insertstmt=("insert into salary(employeeno,name,month,noofdays,noofleaves,overtimeinhours,salary,salaryperday,deduction,extratime,grosspay) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11))
    a.execute(insertstmt)

    #q2
    L1.config(text="Salary Added",fg="#03254c",font=("times",20))
    conn.commit()
    a.close()
    conn.close()
    #############
    print("EMPLOYEENO:%s\nNAME:%s\nMONTH:%s\nNOOFDAYS:%s\nNOOFLEAVES:%s\nOVERTIMEINHOURS%s\nSALARY:%s\nSALARYPERDAY:%s\nDEDUCTION:%s\nEXTRATIME:%s\nGROSSPAY:%s"%(e1.get(),e2.get(),e101.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))


    
master=Tk()
master.title("payroll")
img =Image.open('j1.jpg')
bg = ImageTk.PhotoImage(img)
master.geometry("750x490")
label3 = Label(master, image=bg)
label3.place(x =0,y =0)

label=Label(master,text="ADD SALARY",fg="#03254c",font=("times",20))
label.place(x=300,y=25)
label1=Label(master,text="Employee No.",fg="#03254c",font=("times",15))
label1.place(x=30,y=80)
label2=Label(master,text="Name",fg="#03254c",font=("times",15))
label2.place(x=30,y=110)
label3=Label(master,text="Month",fg="#03254c",font=("times",15))
label3.place(x=30,y=140)
label4=Label(master,text="No. Of Days",fg="#03254c",font=("times",15))
label4.place(x=30,y=170)
label5=Label(master,text="N. Of Leaves",fg="#03254c",font=("times",15))
label5.place(x=30,y=200)

label6=Label(master,text="Overtime(in hrs.)",fg="#03254c",font=("times",15))
label6.place(x=30,y=230)
label7=Label(master,text="Salary",fg="#03254c",font=("times",15))
label7.place(x=30,y=260)
label8=Label(master,text="Salary/day",fg="#03254c",font=("times",15))
label8.place(x=30,y=290)
label9=Label(master,text="Deduction",fg="#03254c",font=("times",15))
label9.place(x=30,y=320)

label10=Label(master,text="Extra time",fg="#03254c",font=("times",15))
label10.place(x=30,y=350)
label11=Label(master,text="Net Pay",fg="#03254c",font=("times",15))
label11.place(x=30,y=380)
label12=Label(master,text="Search Empno",fg="#03254c",font=("times",15))
label12.place(x=30,y=410)
e1=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e2=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")

e4=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e5=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e6=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e7=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e8=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e9=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e10=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e11=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e12=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")

e1.place(x=200,y=80)
e2.place(x=200,y=110)
e101=Entry(master,width=40,bd=4,fg="white",bg="#03254c",font="italic",selectbackground="cyan")
e101.place(x=200,y=140)
e4.place(x=200,y=170)
e5.place(x=200,y=200)
e6.place(x=200,y=230)
e7.place(x=200,y=260)
e8.place(x=200,y=290)
e9.place(x=200,y=320)
e10.place(x=200,y=350)
e11.place(x=200,y=380)
e12.place(x=200,y=410)
Button(master,text="ADD",fg="#03254c",command=add_fields).place(x=30,y=440)
Button(master,text="SEARCH",fg="#03254c",command=search_record).place(x=200,y=440)
Button(master,text="CLOSE",fg="#03254c",command=master.quit).place(x=370,y=440)


L1=Label(master,text="")
L1.place (x=400,y=470)

mainloop()
