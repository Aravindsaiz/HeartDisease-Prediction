import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from final import execution
import os
import sys
root  = Tk()
obj = execution()
root.geometry('800x800')
root.title("HEART DISEASE PREDICTOR")
img = ImageTk.PhotoImage(Image.open("heart.jpg"))
bimg = Label(root, image=img)
bimg.pack()
w = Canvas(root,width =800,height=800)


def selectoutput():
    output = askopenfile(mode ='r', filetypes =[('Data File', '*.data')])
    return output.name

def selectfile():
    file = askopenfile(mode ='r', filetypes =[('Data File', '*.data')])
    print(file.name)
    label3 = Label(w,text ="Executing .....")
    label3.grid(row = 1,column =2)
    obj.execute(file.name,selectoutput())
    label3.config(text="Excecuted")
    label4 = Label(w,text ="output saved to selected output file")
    label4.grid(row = 2,column =0)
    

def newpage():
    os.system('python3 gui2.py')

label1  = Label(w,text = "welcome to Disease prediction System ",width=35)
label2 = Label(w,text="choose the data File")
btn1 = Button(w,text="open",command = selectfile)
btn2 = Button(w,text="outputfile")
btn3 = Button(w,text="check symptoms",command=newpage)
w.pack()
label1.grid(row = 0,column=0,columnspan=5,pady=20,padx=200)
label2.grid(row=1,column=0,padx=2,pady=20)
btn1.grid(row =1,column = 1)
btn3.grid(row=3,column=0,pady=20)
root.mainloop()
