import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry('1200x00')
t.configure(bg='lightblue')

def updatedata():
    db=pymysql.connect(host="localhost",user="root",password="root",database="scm")
    cur=db.cursor()
    xa=int(ea.get())
    xb=int(eb.get())
    xc=int(ec.get())
    xd=eb.get()
    xe=ec.get()
    xf=int(ef.get())
    
    sql="update callclosedata set customerid=%s,engineerid=%s, dateofcall=%s, dateofclose=%s, billamount=%s where callrefno=%s"
    cur.execute(sql,(xb,xc,xd,xe,xf,xa))
    db.commit()
    messagebox.showinfo('hi','data updated')
    db.close()

a=Label(t,text='callrefno',bg='lightblue',width=20)
a.place(x=100,y=100)
ea=Entry(t,width=20)
ea.place(x=400,y=100)
b=Label(t,text='customerid',bg='lightblue',width=20)
b.place(x=100,y=160)
eb=Entry(t,width=40)
eb.place(x=400,y=160)
c=Label(t,text='engineerid',bg='lightblue',width=20)
c.place(x=100,y=220)
ec=Entry(t,width=40)
ec.place(x=400,y=220)
d=Label(t,text='dateofcall',bg='lightblue',width=20)
d.place(x=100,y=280)
ed=Entry(t,width=40)
ed.place(x=400,y=280)
e=Label(t,text='dateofclose',bg='lightblue',width=20)
e.place(x=100,y=340)
ee=Entry(t,width=40)
ee.place(x=400,y=340)
f=Label(t,text='billamount',bg='lightblue',width=20)
f.place(x=100,y=400)
ef=Entry(t,width=40)
ef.place(x=400,y=400)
btn1=Button(t,text='Update',command=updatedata,bg='lightblue',width=10)
btn1.place(x=300,y=500)
t.mainloop()
    
