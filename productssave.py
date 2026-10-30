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
    xb=eb.get()
    xc=int(ec.get())
    xd=int(ed.get())
    xe=int(ee.get())

    sql="insert into products values (%s,%s,%s,%s,%s)"
    cur.execute(sql,(xa,xb,xc,xd,xe))
    db.commit()
    messagebox.showinfo('data inserted')
    db.close() 
    
def finddata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=int(ea.get())
    sql="select phone,catid,warrantyindays,price from products where productid=%s"
    cur.execute(sql,(xa))
    data=cur.fetchone()
    eb.insert(0,data[0])
    ec.insert(0,data[1])
    ed.insert(0,data[2])
    ee.insert(0,data[3])
    
    db.close()
    
def updatedata():
    db=pymysql.connect(host="localhost",user="root",password="root",database="scm")
    cur=db.cursor()
    xa=int(ea.get())
    xb=eb.get()
    xc=int(ec.get())
    xd=int(eb.get())
    xe=int(ec.get())
    
    sql="update products set phone=%s,catid=%s, warrantyindays=%s, price=%s where productid=%s"
    cur.execute(sql,(xb,xc,xa))
    db.commit()
    messagebox.showinfo('hi','data updated')
    db.close()
    
def deletedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=int(ea.get())
    sql="delete from products where productid=%s"
    cur.execute(sql,(xa))
    db.commit()
    messagebox.showinfo('Hi','Data Deleted')
    ea.delete(0,END)
    db.close()
    
def showdata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    sql='select*from products'
    records=''
    cur.execute(sql)
    data=cur.fetchall()
    for m in data:
        records=str(records)+str(m)+'\n'
    db.close()
    ta.insert("1.0",records)
ta=Text(t,width=100,height=20)
ta.place(x=50,y=50)
t.title('products')
a=Label(t,text='productid',bg='lightblue',width=20)
a.place(x=100,y=100)
ea=Entry(t,width=20)
ea.place(x=400,y=100)
b=Label(t,text='phone',bg='lightblue',width=20)
b.place(x=100,y=160)
eb=Entry(t,width=40)
eb.place(x=400,y=160)
c=Label(t,text='catid',bg='lightblue',width=20)
c.place(x=100,y=220)
ec=Entry(t,width=40)
ec.place(x=400,y=220)
d=Label(t,text='warrantyindays',bg='lightblue',width=20)
d.place(x=100,y=280)
ed=Entry(t,width=40)
ed.place(x=400,y=280)
e=Label(t,text='price',bg='lightblue',width=20)
e.place(x=100,y=340)
ee=Entry(t,width=40)
ee.place(x=400,y=340)



btn=Button(t,text='Save',command=savedata,bg='lightblue',width=10)
btn.place(x=200,y=400)
btn1=Button(t,text='Update',command=updatedata,bg='lightblue',width=10)
btn1.place(x=300,y=400)
btn2=Button(t,text='Find',command=finddata,bg='lightblue',width=10)
btn2.place(x=400,y=400)
btn3=Button(t,text='Delete',command=deletedata,bg='lightblue',width=10)
btn3.place(x=500,y=400)
btn=Button(t,text='Show',command=showdata,bg='lightblue',width=10)
btn.place(x=600,y=400)
t.mainloop()
