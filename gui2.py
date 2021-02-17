import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
root = Tk()
root.title("symptoms and precautions checker")
root.geometry("800x800")
search = Entry(root,borderwidth=5,width=20)
def searching():
    s2 = search.get()
    for  i in df1.index:
        s = df1['Disease'][i]
        if s.lower()== s2.lower():
            result(i)
            break
        
def result(i):
    w =Canvas(root,width =800,height=800)
    w.grid(row=3,column=0)
    text1 = Text(w,wrap=WORD,height=5,width=25)
    text = Text(w,wrap=WORD,height=5,width=50)
    string = str(df1['Precaution_1'][i])+" , "+str(df1['Precaution_2'][i])+" , "+str(df1['Precaution_3'][i])+" , "+str(df1['Precaution_4'][i])
    text1.insert(INSERT,string)
    text.insert(INSERT,df2['Description'][i])
    label3 = Label(w,text="Description")
    label3.grid(row=0,column=0)
    label4 = Label(w,text="Immediate precautions")
    label4.grid(row=2,column=0)
    text1.grid(row=3,column=0,padx=50,pady=20)
    text.grid(row=1,column=0,padx=50,pady=20)


label1 = Label(root,text="search for disease")
btn1 = Button(root,text="search",command=searching)
label1.grid(row=0,column=0,pady=20,padx=4)
search.grid(row=1,column=0,pady=10,padx=4)
btn1.grid(row=1,column=4,pady=10,padx=4)
df1 = pd.read_csv("precaution.csv")
df2 = pd.read_csv("Description.csv")



root.mainloop()

