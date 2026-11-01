import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry('800x800')
t.configure(bg='lightblue')

def savedata():
    db=pymysql.connect(host="localhost",user="root",password="root",database="scm")
    cur=db.cursor()
    xa=int(ea.get())
    xb=int(eb.get())
    xc=int(ec.get())
    xd=int(ed.get())
    xe=ee.get()

    sql="insert into products values (%s,%s,%s,%s,%s)"
    cur.execute(sql,(xa,xb,xc,xd,xe))
    db.commit()
    messagebox.showinfo('data inserted')
    db.close() 
    

t.title('callfeedback')
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
d=Label(t,text='feedback',bg='lightblue',width=20)
d.place(x=100,y=280)
ed=Entry(t,width=40)
ed.place(x=400,y=280)
e=Label(t,text='remark',bg='lightblue',width=20)
e.place(x=100,y=340)
ee=Entry(t,width=40)
ee.place(x=400,y=340)



btn=Button(t,text='Save',command=savedata,bg='lightblue',width=10)
btn.place(x=200,y=400)
t.mainloop()
