import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry('800x800')
t.configure(bg='lightblue')

def updatedata():
    db=pymysql.connect(host="localhost",user="root",password="root",database="scm")
    cur=db.cursor()
    xa=int(ea.get())
    xb=eb.get()
    xc=ec.get()
    xd=ed.get()
    xe=int(ee.get())
    sql="update servicecentre set name=%s,address=%s,email=%s, regno=%s where id=%s"
    cur.execute(sql,(xb,xc,xd,xe,xa))
    db.commit()
    messagebox.showinfo('hi','data updated')
    db.close()

t.title('Servicecentre')    
a=Label(t,text='id',bg='lightblue',width=20)
a.place(x=100,y=100)
ea=Entry(t,width=20)
ea.place(x=400,y=100)
b=Label(t,text='name',bg='lightblue',width=20)
b.place(x=100,y=160)
eb=Entry(t,width=40)
eb.place(x=400,y=160)
c=Label(t,text='address',bg='lightblue',width=20)
c.place(x=100,y=220)
ec=Entry(t,width=40)
ec.place(x=400,y=220)
d=Label(t,text='email',bg='lightblue',width=20)
d.place(x=100,y=280)
ed=Entry(t,width=40)
ed.place(x=400,y=280)
e=Label(t,text='regno',bg='lightblue',width=20)
e.place(x=100,y=340)
ee=Entry(t,width=40)
ee.place(x=400,y=340)



btn1=Button(t,text='Update',command=updatedata,bg='lightblue',width=10)
btn1.place(x=300,y=400)

t.mainloop()

