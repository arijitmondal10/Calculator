import tkinter
from tkinter import *

temp = Tk()

temp.title("Calculator")
temp.geometry("570x600+100+200")
temp.resizable(False,False)
temp.configure(bg = "#17160c")

eq = ""

def clear():
    global eq
    eq = ""
    label_result.config(text = eq)

def show(value):
    global eq
    eq+=value
    label_result.config(text = eq)

def calculate():
    global eq
    result =""
    if eq != "":
        try:
             result = eval(eq)
             eq = str(result)  
             label_result.config(text=eq)
        except:
            result = "Error"
            eq =""
            label_result.config(text = result)
    



label_result = Label(temp,width=25,height = 2,font =("arial",30))
label_result.pack()

Button(temp,text = "C",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#3697f5",command = lambda: clear()).place(x=10,y=100)
Button(temp,text = "/",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("/")).place(x=150,y=100)
Button(temp,text = "%",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("%")).place(x=290,y=100)
Button(temp,text = "*",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#3697f5",command = lambda: show("*")).place(x=430,y=100)

Button(temp,text = "7",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("7")).place(x=10,y=200)
Button(temp,text = "8",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("8")).place(x=150,y=200)
Button(temp,text = "9",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("9")).place(x=290,y=200)
Button(temp,text = "+",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("+")).place(x=430,y=200)

Button(temp,text = "4",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("4")).place(x=10,y=300)
Button(temp,text = "5",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("5")).place(x=150,y=300)
Button(temp,text = "6",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("6")).place(x=290,y=300)
Button(temp,text = "-",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("-")).place(x=430,y=300)

Button(temp,text = "1",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("1")).place(x=10,y=400)
Button(temp,text = "2",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("2")).place(x=150,y=400)
Button(temp,text = "3",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("3")).place(x=290,y=400)
Button(temp,text = "0",width = 11,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show("0")).place(x=10,y=500)

Button(temp,text = ".",width = 5,height =1,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#2a2d36",command = lambda: show(".")).place(x=290,y=500)
Button(temp,text = "=",width = 5,height =3,font = ("arial",30,"bold"),bd=1,fg= "#fff",bg="#8c3d04",command = lambda: calculate()).place(x=430,y=400)

temp.mainloop()