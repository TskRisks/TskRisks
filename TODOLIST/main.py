import tkinter as tk
from tkinter import *
from datetime import datetime, timedelta

window=Tk()
window.title("To do list")
window.geometry("400x600+400+10")
window.resizable(False,False)

ListTask=[]
checklist=[]

def addTask():
    task= Tentry.get()
    Tentry.delete(0,END)
    
    if task:
        todaydate=datetime.now().strftime("%m-%d-%y")
        timestamp=datetime.now().strftime(" %I:%M%p")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m-%d-%y")

        task_with_timestamp = task + "  | " +  todaydate + " " + timestamp
        tomorrowdate = task + "  | " + tomorrow + " " + todaydate
        
        with open("tasklist.txt", 'a') as filelist:
            filelist.write(f"\n{task_with_timestamp}")
        ListTask.append(task_with_timestamp)
        lbox.insert( END, task_with_timestamp)

def delTask():
    global ListTask
    task=str(lbox.get(ANCHOR))
    if task in ListTask:
        ListTask.remove(task)
        with open("tasklist.txt",'w') as filelists:
            for task in ListTask:
                filelists.write(task+"\n")
                
        lbox.delete( ANCHOR)
        
def openFileList():
    try:
        global ListTask
        with open("tasklist.txt","r") as filelist:
            tasks = filelist.readlines()
        
        for task in tasks:
            if task != '\n':
                ListTask.append(task)
                lbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()

Icon=PhotoImage(file="png/1.png")
window.iconphoto(False,Icon)

navbar=Frame(window,bg="#2D4356", width=400, height=100,highlightthickness=0)
navbar.place(x=0,y=30)
pname=tk.Label(window, text="To do List", font=("Times New Roman", 30, 'bold'),fg="white",bg="#2D4356")
pname.place(x=35,y=55)

Iicon=PhotoImage(file="png/3.png")
Label(window,image=Iicon,bg="#2D4356").place(x=300,y=55)

frame=Frame(window,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
Tentry=Entry(frame,width=18,font="Times 20",bd=0)
Tentry.place(x=10,y=7)
Tentry.focus()

addbutton=Button(frame, text="ADD",font=("times new roman",20,"bold"),width=6, bg="#00FFCA",fg="#0A4D68",bd=0, command=addTask)
addbutton.place(x=300,y=0)

lframe=Frame(window,width=700,height=280,bg="#05BFDB",bd=3)
lframe.pack(pady=(240,60))

lbox=Listbox(lframe,font=("times new roman",12,"bold"),width=40,height=60,bg="#05BFDB",fg="black",cursor="hand2",selectbackground="#5a59ff")
lbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(lframe)
scrollbar.pack(side=RIGHT, fill=BOTH)

lbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbox.yview)

openFileList()

delbutton=PhotoImage(file="png/4.png")
Button(window,image=delbutton,bd=0, command=delTask).place(x=170,y=540)

window.mainloop()