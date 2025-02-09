import tkinter as tk
from tkinter import *
root=tk.Tk ()
# root.geometry("387x258")
root.config(bg="#333333")
calculations=" "

def add_to_calculations(symbol):
    global calculations
    calculations+=symbol
    T_entry.delete(1.0,END)
    T_entry.insert(1.0,calculations)
def calculate():
    try:
        global calculations
        calculations=eval(calculations)
        T_entry.delete(1.0,END)
        T_entry.insert(1.0,calculations)
        calculations=""
    except ZeroDivisionError:
        T_entry.delete(1.0,END)
        T_entry.insert(1.0,"Error: Division by zero")
    except Exception :
        T_entry.delete(1.0,END)
        T_entry.insert(1.0,"Error!")
           
def clear ():
    global calculations
    calculations=""
    T_entry.delete(1.0,END)

clear_button=Button(root,text="C",command=clear,font=("arial",14), bd=1, width=6, background="orange",foreground="black")
equal_button=Button(root,text="=",command=calculate,font=("arial",14), bd=1, width=6, background="orange",foreground="black")
point_button=Button(root,text=".",command=lambda:add_to_calculations("."),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
modulus_button=Button(root,text="%",command=lambda:add_to_calculations("%"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
multiplication_button=Button(root,text="*",command=lambda:add_to_calculations("*"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
division_button=Button(root,text="/",command=lambda:add_to_calculations("/"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
open_bracket=Button(root,text="(",command=lambda:add_to_calculations("("),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
close_bracket=Button(root,text=")",command=lambda:add_to_calculations(")"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
minus_button=Button(root,text="-",command=lambda:add_to_calculations("-"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")
plus_button=Button(root,text="+",command=lambda:add_to_calculations("+"),font=("arial",14), bd=1, width=6, background="grey",foreground="black")


clear_button.grid(row=4,column=3,sticky="news")
equal_button.grid(row=5,column=3,sticky="news")
point_button.grid(row=5,column=2,sticky="news")
modulus_button.grid(row=5,column=0,sticky="news")
minus_button.grid(row=2,column=3,sticky="news")
plus_button.grid(row=3,column=3,sticky="news")
multiplication_button.grid(row=1,column=3,sticky="news")
division_button.grid(row=1,column=2,sticky="news")
open_bracket.grid(row=1,column=0,sticky="news")
close_bracket.grid(row=1,column=1,sticky="news")


button_1 = Button(root, text=1, command=lambda: add_to_calculations("1"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_2 = Button(root, text=2, command=lambda: add_to_calculations("2"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_3 = Button(root, text=3, command=lambda: add_to_calculations("3"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_4 = Button(root, text=4, command=lambda: add_to_calculations("4"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_5 = Button(root, text=5, command=lambda: add_to_calculations("5"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_6 = Button(root, text=6, command=lambda: add_to_calculations("6"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_7 = Button(root, text=7, command=lambda: add_to_calculations("7"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_8 = Button(root, text=8, command=lambda: add_to_calculations("8"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_9 = Button(root, text=9, command=lambda: add_to_calculations("9"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")
button_0 = Button(root, text=0, command=lambda: add_to_calculations("0"), font=("arial", 14), bd=1, width="6", background="light grey", foreground="black")



button_1.grid(row=2,column=0,sticky="news")
button_2.grid(row=2,column=1,sticky="news")
button_3.grid(row=2,column=2,sticky="news")
button_4.grid(row=3,column=0,sticky="news")
button_5.grid(row=3,column=1,sticky="news")
button_6.grid(row=3,column=2,sticky="news")
button_7.grid(row=4,column=0,sticky="news")
button_8.grid(row=4,column=1,sticky="news")
button_9.grid(row=4,column=2,sticky="news")
button_0.grid(row=5,column=1,sticky="news")


T_entry=tk.Text(root,width=10,height=2,font=("arial",12))
T_entry.grid(row=0,columnspan=4,sticky ="news") 

root.mainloop()