from  tkinter import *
from  tkinter import messagebox
from  tkinter import ttk
from Eempolyee import *
obj=database("Employee.db")

window=Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry("1500x800")
#variables
name=StringVar()
empid=StringVar()
age=StringVar()
address=StringVar()
dob=StringVar()
mail=StringVar()
contact=StringVar()
cobox=StringVar()

frame1=Frame(window,highlightbackground="black",highlightthickness=4)
frame1.pack(fill=BOTH)

lb_n=Label(frame1,text="NAME",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_n.grid(row=2,column=0)
txtn=Entry(frame1,width=30,textvariable=name,font=("times",18,"bold"),fg="blue")
txtn.grid(row=2,column=1)

lb_epid=Label(frame1,text="EMP_ID",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_epid.grid(row=1,column=0)
txtid=Entry(frame1,width=30,textvariable=empid,font=("times",18,"bold"),fg="blue")
txtid.grid(row=1,column=1)

lb_n=Label(frame1,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times",25,"italic"),pady=10,padx=10,fg="green")
lb_n.grid(row=0,column=0,columnspan=6)


lb_age=Label(frame1,text="AGE",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_age.grid(row=3,column=0)
txtage=Entry(frame1,width=30,textvariable=age,font=("times",18,"bold"),fg="blue")
txtage.grid(row=3,column=1)

lb_add=Label(frame1,text="ADDRESS",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_add.grid(row=4,column=0)
txtadd=Entry(frame1,width=30,textvariable=address,font=("times",18,"bold"),fg="blue")
txtadd.grid(row=4,column=1)

lb_DOB=Label(frame1,text="DOB",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_DOB.grid(row=5,column=0)
txtDOB=Entry(frame1,width=30,textvariable=dob,font=("times",18,"bold"),fg="blue")
txtDOB.grid(row=5,column=1)

lb_CO=Label(frame1,text="GENDER",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_CO.grid(row=1,column=3)
combox=ttk.Combobox(frame1,width=30,textvariable=cobox,font=("times",18,"bold"),state='readonly')
combox.grid(row=1,column=4)
combox["value"]=("MALE","FEMALE",'OTHERS')
combox.config()

lb_ct=Label(frame1,text="CONTACT",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_ct.grid(row=2,column=3)
txtct=Entry(frame1,width=30,textvariable=contact,font=("times",18,"bold"),fg="blue")
txtct.grid(row=2,column=4)

lb_mail=Label(frame1,text="MAIL",font=("times",18,"bold"),pady=10,padx=10,fg="black")
lb_mail.grid(row=3,column=3)
txtMAIL=Entry(frame1,width=30,textvariable=mail,font=("times",18,"bold"),fg="blue")
txtMAIL.grid(row=3,column=4)

def getrecord(event):
    rec=tv.focus()
    data=tv.item(rec)
    global row
    row=data["values"]
    empid.set(row[0])
    name.set(row[1])
    age.set(row[2])
    address.set(row[3])
    dob.set(row[4])
    mail.set(row[5])
    combox.set(row[7])
    contact.set(row[6])
    #mail.set(row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in obj.fetch():
        tv.insert("",END,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],[7]))

def insert():
    if txtid.get()=="" or txtn.get()=="" or txtage.get()=="" or txtadd.get()=="" or txtDOB.get()=="" or combox.get()=="" or txtct.get()=="" or txtMAIL.get()=="":
        messagebox.showwarning("Message","please Enter all Details")
    else:
        obj.insert(txtid.get(),txtn.get(),txtage.get(),txtadd.get(),txtDOB.get(),combox.get(),txtct.get(),txtMAIL.get())
        messagebox.showinfo("Message","Record insert sucessfully")
        cleare()
        displayall()

def update():
    if txtid.get() == "" or txtn.get() == "" or txtage.get() == "" or txtadd.get() == "" or txtDOB.get() == "" or combox.get() == "" or txtct.get() == "" or txtMAIL.get() == "":
        messagebox.showwarning("Message", "please Enter all Details")
    else:
        obj.update(txtid.get(),txtn.get(),txtage.get(),txtadd.get(),txtDOB.get(),combox.get(),txtct.get(),txtMAIL.get())
        messagebox.showinfo("Message", "update sucessfully")
        cleare()
        displayall()

def delete():
    obj.delete(row[0])
    cleare()
    displayall()
def cleare():
    name.set("")
    empid.set("")
    age .set("")
    address.set("")
    dob.set("")
    mail.set("")
    contact.set("")
    combox.set("")
    messagebox.showinfo("Message","cleare sucessfully")


#butten frame
btnsub=Button(frame1,text="INSERT",font=("times",15,"bold"),padx=4,pady=4,fg="white",bg="green",bd=0,command=insert)
btnsub.grid(row=6,column=0,padx=20,pady=20)

btnup=Button(frame1,text="UPDATE",font=("times",15,"bold"),padx=4,pady=4,fg="white",bg="gray",bd=0,command=update)
btnup.grid(row=6,column=1,pady=20)

btnDL=Button(frame1,text="DELETE",font=("times",15,"bold"),padx=4,pady=4,fg="white",bg="red",bd=0,command=delete)
btnDL.grid(row=6,column=2,pady=20)
btnclr=Button(frame1,text="CLEAR",font=("times",15,"bold"),padx=4,pady=4,fg="white",bg="orange",bd=0,command=cleare)
btnclr.grid(row=6,column=4,pady=20)

#tree frame 2

tree_frame=Frame(window)
tree_frame.place(x=0,y=400,width=1500,height=400)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("times",18,"bold"),rowhight=50)
style.configure("mystyle.Treeview.headings",font=("times",18,"bold"))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8))
tv.heading("1",text="EMP_ID")
tv.column("1",width=5)
tv.heading("2",text="NAME")
tv.column("2",width=15)
tv.heading("3",text="AGE")
tv.column("3",width=5)
tv.heading("4",text="ADDRESS")
tv.column("4",width=15)
tv.heading("5",text="DOB")
tv.column("5",width=10)
tv.heading("6",text="GENDER")
tv.column("6",width=5)
tv.heading("7",text="CONTACT")
tv.column("7",width=10)
tv.heading("8",text="MAIL_ID")
tv.column("8",width=15)
tv["show"]="headings"

tv.bind("<ButtonRelease-1>",getrecord)
tv.pack(fill=X)






displayall()
window.mainloop()