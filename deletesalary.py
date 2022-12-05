from tkinter import*
from PIL import ImageTk, Image  
import pymysql
import pymysql.cursors


def search_record():
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    args=int(e12.get())
    sql="SELECT * FROM salary where employeeno=%d"%(args)
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
            e1.insert(0,empno)
            e2.insert(1,name)
            e101.insert(2,month)
            e4.insert(3,ndays)
            e5.insert(4,nleaves)
            e6.insert(5,otime)
            e7.insert(6,salary)
            e8.insert(7,spday)
            e9.insert(8,deduct)
            e10.insert(9,etime)
            e11.insert(10,gpay)
           
    except:
        print("ERROR")
        a.close()
        conn.close()
def delete_record():
    conn=pymysql.connect(host='localhost',user='root',db='payroll')
    a=conn.cursor()
    args=int(e12.get())
    delstmt="DELETE FROM salary where employeeno=%d"%(args)
    L1.config(text="Salary Deleted",fg="#3a4c40",font=("times",20))
    a.execute(delstmt)
    print("RECORD DELETED")
    conn.commit()
    a.close()
    conn.close()

   


master=Tk()
master.title("payroll")
img =Image.open('j1.jpg')
bg = ImageTk.PhotoImage(img)
master.geometry("780x520")
label3 = Label(master, image=bg)
label3.place(x =0,y =0)

label=Label(master,text="DELETE SALARY",fg="#3a4c40",font=("times",20))
label.place(x=300,y=25)
label1=Label(master,text="Employee No.",fg="#3a4c40",font=("times",15))
label1.place(x=30,y=80)
label2=Label(master,text="Name",fg="#3a4c40",font=("times",15))
label2.place(x=30,y=110)
label3=Label(master,text="Month",fg="#3a4c40",font=("times",15))
label3.place(x=30,y=140)
label4=Label(master,text="No. Of Days",fg="#3a4c40",font=("times",15))
label4.place(x=30,y=170)
label5=Label(master,text="N. Of Leaves",fg="#3a4c40",font=("times",15))
label5.place(x=30,y=200)

label6=Label(master,text="Overtime(in hrs.)",fg="#3a4c40",font=("times",15))
label6.place(x=30,y=230)
label7=Label(master,text="Salary",fg="#3a4c40",font=("times",15))
label7.place(x=30,y=260)
label8=Label(master,text="Salary/day",fg="#3a4c40",font=("times",15))
label8.place(x=30,y=290)
label9=Label(master,text="Deduction",fg="#3a4c40",font=("times",15))
label9.place(x=30,y=320)

label10=Label(master,text="Extra time",fg="#3a4c40",font=("times",15))
label10.place(x=30,y=350)
label11=Label(master,text="Gross Pay",fg="#3a4c40",font=("times",15))
label11.place(x=30,y=380)
label12=Label(master,text="Search Employee No.",fg="#3a4c40",font=("times",15))
label12.place(x=30,y=410)
e1=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e2=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")

e4=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e5=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e6=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e7=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e8=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e9=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e10=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e11=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
e12=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")

e1.place(x=200,y=80)
e2.place(x=200,y=110)
e101=Entry(master,width=40,bd=4,fg="white",bg="#3a4c40",font="italic",selectbackground="cyan")
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
Button(master,text="Delete",fg="#3a4c40",command=delete_record).place(x=30,y=440)
Button(master,text="Search",fg="#3a4c40",command=search_record).place(x=200,y=440)
Button(master,text="Close",fg="#3a4c40",command=master.quit).place(x=370,y=440)


L1=Label(master,text="")
L1.place (x=400,y=470)

mainloop()
