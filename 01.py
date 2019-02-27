import tkinter
from tkinter import *
import random
top = Tk()
top.title("缘分检测器")

f1 = Frame(top)
L1 = Label(f1,text="你的名字")
L1.pack(side=LEFT)
E1 = Entry(f1,width =30,bd = 2,fg = "green",cursor = "plus")
E1.pack(side = RIGHT)
f1.pack()
f2 = Frame(top)
L2 = Label(f2,text="TA的名字")
L2.pack(side=LEFT)
E2 = Entry(f2,width =30,bd = 2,fg = "red",cursor = "circle")
E2.pack(side = LEFT)
f2.pack()
f3 = Frame(top)
def function():
    aa = random.randint(0,100)
    print ("你们的缘分值是：",aa)
    return
b = tkinter.Button(top,text = "马上测缘分",activeforeground = "black",command = function,padx = 5,pady = 5)
b.pack(side = RIGHT)
f3.pack()
print()
top.mainloop()