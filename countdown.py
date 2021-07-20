import time as temps
from tkinter import *
from tkinter import messagebox
from datetime import datetime




def countdown(t):
    root=Tk()
    a=Text(root, height=2, width=30)
    a.pack()
    a.insert(END,'remaining time:  ' )
    wakt=int(t)
    time=divmod(wakt, 60)
    while time[0]+time[1]>0:
        wakt-=1
        time=divmod(wakt, 60)
        dt_obj = datetime( 2000,3,3,23,time[0], time[1])
        final_t=dt_obj.strftime("%M:%S")
        root.update()
        a.delete("1.17","end")
        a.insert(END,final_t )
        temps.sleep(1)
        
    messagebox.showinfo(title='info', message='Fire In The Hole')
    root.mainloop()
    
   
countdown(input('enter time in s'))




