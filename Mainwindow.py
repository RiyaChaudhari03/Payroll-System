from tkinter import*
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror
from PIL import ImageTk, Image  
import sys,os
def AddEmployee():
    os.system('AddEmployee.py')
    print("Add Employee")
def DeleteEmployee():
    os.system('DeleteEmployee.py')
def UpdateEmp():
   os.system('UpdateEmp1.py')
def ViewEmployee():
    os.system('ViewEmployee.py')
def AddSalary():
    os.system('AddSalary.py')
def DeleteSalary():
    os.system('DeleteSalary.py')
def UpdateSalary():
    os.system('UpdateSalary.py')
def ViewSalary():
    os.system('ViewSalary.py')
root=Tk()
menu=Menu(root)
root.config(menu=menu)
root.title("Payroll Management System")

employeemenu=Menu(menu)
menu.add_cascade(label="Employee",menu=employeemenu)
employeemenu.add_command(label="Add Employee",command=AddEmployee)
employeemenu.add_command(label="Delete Employee",command=DeleteEmployee)
employeemenu.add_command(label="Update Employee",command=UpdateEmp)
employeemenu.add_command(label="View Employee",command=ViewEmployee)
employeemenu.add_command(label="Exit",command=root.quit)
salarymenu=Menu(menu)
menu.add_cascade(label="Salary",menu=salarymenu)
salarymenu.add_command(label="Add Salary",command=AddSalary)
salarymenu.add_command(label="Delete Salary",command=DeleteSalary)
salarymenu.add_command(label="Update Salary",command=UpdateSalary)
salarymenu.add_command(label="View Salary",command=ViewSalary)
salarymenu.add_command(label="Exit",command=root.quit)


img =Image.open('j1.jpg')
bg = ImageTk.PhotoImage(img)
root.geometry("850x650")
label = Label(root, image=bg)
label.place(x = 0,y = 0)
label2 = Label(root, text = "Payroll Management System",fg="Blue",
font=("Arial Black", 40))
label2.pack(pady = 10)
mainloop()





                 
                 
